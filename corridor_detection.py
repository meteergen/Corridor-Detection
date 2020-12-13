# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CorridorDetection 
                                 A QGIS plugin
 This plugin detects corridors on road network
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-10-09
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Metehan Ergen / Hacettepe University | Politecnico di Milano
        email                : metehan.ergenn@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
""" 
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction ,QMessageBox, QFileDialog, QInputDialog
from qgis.core import *
from qgis.gui import QgsMapToolIdentifyFeature, QgsMapToolIdentify, QgsMapToolPan  #Imported manually
from qgis.utils import iface                                         #Imported manually
from PyQt5.QtCore import QVariant, Qt, QDateTime
from PyQt5.QtGui import *


# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .corridor_detection_dialog import CorridorDetectionDialog
from .corridor_detection_selection_dialog import SelectionDialog

import os.path
import csv
import networkx as nx
import math
import datetime
import time




        

class CorridorDetection():
    """QGIS Plugin Implementation."""
    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'CorridorDetection_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Corridor Detection')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
       
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('CorridorDetection', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToVectorMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/corridor_detection/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Detect Corridors'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginVectorMenu(
                self.tr(u'&Corridor Detection'),
                action)
            self.iface.removeToolBarIcon(action)

    
    # Clear fields on dialog when plugin started
    def clear_fields(self):
        """Clearing the fields when layers are changed"""
        self.dlg.fieldsComboBox.clear()

    # Clear elements on dialog when plugin started
    def clear_ui(self): # Check whether load_comboBox() method is going to be called at the end of this method
        """Clearing the UI for new operations"""
        self.dlg.layerComboBox.clear()
        self.dlg.lineEdit.clear()

    # When field changed, changed that also in the selectTool class
    def changeField(self,fieldNamesLayer):
        if not self.t == 0:
            self.t.nodes = []
            self.t.field = fieldNamesLayer[self.dlg.fieldsComboBox.currentIndex()]

    # Error message box to warn user (input: warning text)
    def error_msg(self,text):
        QMessageBox.warning(self.dlg.show(), self.tr("Corridor Detection:Warning"),
                            self.tr(str(text)), QMessageBox.Ok )
    def success_msg(self,text):
        QMessageBox.information(self.dlg.show(), self.tr("Corridor Detection:Information"),
                            self.tr(str(text)), QMessageBox.Ok )
    
    # Dijktras Algorithm for detection of corridors
    def runAlgorithm(self):
        t0 = time.time()


        
        self.corridor_segments = self.t.nodes[::-1]
        
        if len(self.corridor_segments) < 2:
            self.error_msg("Select at least two segments !")
            return False
        # Create a directed graph
        G = nx.DiGraph()

        # Add the segments to the graph 
        # The cost of each segment is assumed to be 1 - this could be updated for different purposes
        for segment in self.adj_matrix:
            for neigh in range(len(self.adj_matrix[segment])):
                G.add_weighted_edges_from( [(segment, self.adj_matrix[segment][neigh], {'distance':1})] ) 
        
        self.path = []
        for c in range(len(self.corridor_segments)-1):
            temp_path = nx.shortest_path(G, source = self.corridor_segments[c], target = self.corridor_segments[c+1])
            # Remove the last element in the path - it will be included in the next iteration
            temp_path.pop()
            # if we path.append(temp_path), we will generate a 2D list. Instead copy each segment one-by-one
            for i in range(len(temp_path)):
                self.path.append(temp_path[i])

        # Add the last segment of the corridor
        self.path.append(self.corridor_segments[c+1])
    
        # str1 = "["+', '.join(str(e) for e in self.path)+"]"
        # self.dlg.textBrowser_2.setText(str(str1))

        # Fix: they should be selected by their object id's.
        self.t.selectFeatures(self.path)
        #self.selectedLineLayer.selectByExpression(res)
        t1 = time.time()
        total = t1-t0
        print("runtime: ",total)

    def visualize(self):
        if not len(self.path) < 1:
            epoch = datetime.datetime.fromisoformat('2020-01-01T10:00:00')
            #epoch = QDateTime.fromString('2020-12-12 12:00:00','yyyy-MM-dd hh:mm:ss')
            
            idx = self.selectedLineLayer.fields().indexFromName("time")
            attr_map = {}
            for node in self.path:
                for selectedFeature in self.selectedLineLayer.selectedFeatures():
                    if node == selectedFeature[self.t.field]:
                        #epoch.addSecs(30) # days, seconds, then other fields.
                        formatted = epoch.strftime('%Y-%m-%dT%H:%M:%S')
                        epoch = epoch + datetime.timedelta(0,1)
                        attr_map[selectedFeature.id()] = {idx: formatted }

            self.selectedLineLayer.dataProvider().changeAttributeValues(attr_map)
                

        
        
    # Load layers and fields to combobox when index changed
    def load_comboBox(self):
        """Load the fields into combobox when layers are changed"""
        lineLayers_shp = []
        
        layers = [layer for layer in QgsProject.instance().mapLayers().values()]
        if len(layers) != 0:  # checklayers exist in the project
            for layer in layers:
                if hasattr(layer, "dataProvider"):  # to not consider Openlayers basemaps in the layer list
                    myfilepath = layer.dataProvider().dataSourceUri()  # directory including filename
                    (myDirectory, nameFile) = os.path.split(myfilepath)  # splitting into directory and filename
                    #if (".shp" in nameFile):
                    try:
                        if layer.geometryType() == 1:
                            lineLayers_shp.append(layer)    # Exception for OSM base map (Raster)
                    except:
                        continue
                
        self.selectedLineLayerIndex = self.dlg.layerComboBox.currentIndex()
        
        if self.selectedLineLayerIndex < 0 or self.selectedLineLayerIndex > len(lineLayers_shp):
            return
        try:
            self.selectedLineLayer = lineLayers_shp[self.selectedLineLayerIndex]
        except:
            return
        
        fieldNamesLayer = [field.name() for field in self.selectedLineLayer.fields()]
        
        self.clear_fields()
        self.dlg.fieldsComboBox.addItems(fieldNamesLayer)

        if not self.t == 0:
            self.t.field = fieldNamesLayer[self.dlg.fieldsComboBox.currentIndex()]
            self.t.active_changed(self.selectedLineLayer)
            self.iface.mapCanvas().setMapTool(self.t)

        self.dlg.fieldsComboBox.currentIndexChanged.connect(lambda: self.changeField(fieldNamesLayer))
        

    # Load layers to combobox when plugin started
    def loadLayerList(self):
   
        lineLayersList = []
        lineLayers_shp = []
        # Show the shapefiles in the ComboBox
        layers = [layer for layer in QgsProject.instance().mapLayers().values()]
        if len(layers) != 0:  # checklayers exist in the project
            for layer in layers:
                if hasattr(layer, "dataProvider"):  # to not consider Openlayers basemaps in the layer list
                    myfilepath = layer.dataProvider().dataSourceUri()  # directory including filename
                    (myDirectory, nameFile) = os.path.split(myfilepath)  # splitting into directory and filename
                    #if (".shp" in nameFile):
                    try:
                        if layer.geometryType() == 1:               # Exception for OSM base map (Raster)
                            lineLayersList.append(layer.name())
                            lineLayers_shp.append(layer)
                    except:
                        continue
                  
            # Layer lists
            self.dlg.layerComboBox.addItems(lineLayersList)
         
            # Point and Polygon layer indexes
            self.selectedLineLayerIndex = self.dlg.layerComboBox.currentIndex()
        
            if self.selectedLineLayerIndex < 0 or self.selectedLineLayerIndex > len(lineLayers_shp):
                return

            # Selected layers
            self.selectedLineLayer = lineLayers_shp[self.selectedLineLayerIndex]

            fieldNamesLayer = [field.name() for field in self.selectedLineLayer.fields()]

            # Button clicks etc.
            self.dlg.pushButton.clicked.connect(lambda: self.t.deactivate()) #Deactivate # might need a disconnect
            self.dlg.layerComboBox.currentIndexChanged.connect(lambda: self.load_comboBox()) # might need a disconnect
            self.dlg.returnSelectionButton.clicked.connect(lambda : self.t.selectPrevious()) # might need a disconnect
           
            self.clear_fields()
            self.dlg.fieldsComboBox.addItems(fieldNamesLayer)
            
            return [layers, lineLayers_shp, fieldNamesLayer]
        else: 
            return [layers, False]
    

    # Open input dialog for selecting between twin segments
    def inputDialog(self,firstSegment,secondSegment):
        text, ok = QInputDialog.getText(self.dlg, 'Input Dialog', '(1) :'+str(firstSegment)+' \n(2) :'+str(secondSegment))
        if ok:
            return text

    # Display path on text browser
    def displayPath(self,path): 
        str1 = "["+', '.join(str(e) for e in path)+"]"
        self.dlg.textBrowser.setText(str(str1))

    # Select adjacency matrix file
    def select_adj_file(self):     
        filename, _filter = QFileDialog.getOpenFileName(self.dlg, "Select adj file ")
        self.dlg.lineEdit.setText(filename)

        # Create empty dictionaries
        adj_matrix = dict()
        #visited = dict()
        print("TEST PROTOCOL 444")
        print(self.dlg.lineEdit.text())
        
        # Open the adjacency matrix provided
        try:
            with open(self.dlg.lineEdit.text()) as csv_file:    
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    """
                    if line_count == 0:
                        line_count += 1
                    elif(line_count==1): # strangely there is an empty line
                        line_count += 1
                    elif(line_count>=1):
                    """
                    #print("Eleman sayisi: ", len(row), row)
                    adj_matrix[row[0]] = row[1:len(row)]
                    #visited[row[0]] = False
                    #print("Segment", row[0], "'s neighbors:",  adj_matrix[row[0]])
                    line_count += 1
        except:
            self.error_msg("Please select a proper adjacency matrix file !")
            return False
        self.adj_matrix = adj_matrix

    def select_output_file(self):
        filename = QFileDialog.getExistingDirectory(self.dlg, "Select output file ")
        self.dlg.lineEdit_2.setText(filename)

    def export_to_csv(self):
        # There is a better control need
        if len(self.dlg.lineEdit_3.text()) < 2:
            self.error_msg("Please type the corridor id !")
            return False

        if len(self.dlg.lineEdit_2.text()) < 2:
            self.error_msg("Please select the output csv file")
            return False
            
        csvHeader = self.selectedLineLayer.fields().names()
        features = self.selectedLineLayer.selectedFeatures()
        csvHeader.append("corridor_id")
        csvHeader.append("geometry")
        
        with open(self.dlg.lineEdit_2.text()+'/'+self.dlg.lineEdit_3.text()+'.csv', "w",newline = "") as f:
            writer = csv.writer(f)
            for node in self.path:
                for feature in features:
                    if str(feature[self.t.field]) == str(node):
                        feature2write = feature.attributes()[0]
                        writer.writerow([feature2write])
            f.close()
            self.success_msg("Data successfully exported")

            self.selectedLineLayer.startEditing()
            for feature in features:
                feature["visited"] = 1
                self.selectedLineLayer.updateFeature(feature)
            self.selectedLineLayer.commitChanges()
            
    def prepare_layer(self):
       
        # Add selected field for rule based selection
        fields = self.selectedLineLayer.fields().names()
        fields2add = ["visited","time"]
        dp = self.selectedLineLayer.dataProvider()
        for name in fields2add:
            if not name in fields:
                if name == 'time':
                    dateField = QgsField(name,QVariant.DateTime)
                    dateField.setLength(50)
                    dp.addAttributes([dateField])
                else:
                    dp.addAttributes([QgsField(name,QVariant.Int)])
            elif name == 'visited':
                idx = self.selectedLineLayer.fields().indexFromName('visited')
                if not idx == -1:
                    dp.deleteAttributes([idx])
                    dp.addAttributes([QgsField(name,QVariant.Int)])
        self.selectedLineLayer.updateFields()

        stylePath = "/styles/layerStyle.qml"
        self.selectedLineLayer.loadNamedStyle(os.path.dirname(__file__) + stylePath)

    # Send the selected button valueo to SelectTool class (There might be a convenient way)
    def buttonValue(self,val):
        self.t.buttonValue = val
                
    def run(self):
        """Run method that performs all the real work"""
        

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg_Selection = SelectionDialog()
            # Really important: The only way to pass arguments to a function with connect is lambda
            self.dlg_Selection.firstButton.clicked.connect(lambda: self.buttonValue(0))
            self.dlg_Selection.secondButton.clicked.connect(lambda: self.buttonValue(1))
            self.dlg = CorridorDetectionDialog()            
            self.dlg.toolButtonAdj.clicked.connect(self.select_adj_file)
            self.dlg.toolButtonOut.clicked.connect(self.select_output_file)
            self.dlg.pushButton_2.clicked.connect(self.runAlgorithm)
            self.dlg.pushButton_csv.clicked.connect(self.export_to_csv)
            self.dlg.prepareButton.clicked.connect(self.prepare_layer)
            self.dlg.visualizeButton.clicked.connect(self.visualize)

            # Make gui always in front of qgis
            self.dlg.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.dlg_Selection.setWindowFlags(Qt.WindowStaysOnTopHint)
            
            
        self.clear_ui()
        try:
            layers, lineLayers_shp, fieldNamesLayer = self.loadLayerList()
            if len(layers) == 0:
                return
        except:
            iface.messageBar().pushMessage("Error", "There is no vector layer on interface", level=Qgis.Critical)
            return
        

        # show the dialog
        self.dlg.show()
        
        selectedLayerIndex = self.dlg.layerComboBox.currentIndex()
        selectedLayer = lineLayers_shp[selectedLayerIndex]

        self.t = selectTool(self.iface,selectedLayer,self)
        
        #self.t.featureIdentified.connect(self.t.onFeatureIdentified) # Selecting only one
        
        self.load_comboBox()
        
        # Run the dialog event loop
        result = self.dlg.exec_()

           
        # See if OK was pressed
        if result:
            self.adj_matrix = False
            pass
          
class selectTool(QgsMapToolIdentifyFeature):

    def __init__(self, iface, layer, obj):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.layer = layer
        self.nodes = []
        self.obj = obj
        self.field = ""
        self.deselectedSegmentIndex = False
        self.buttonValue = False
        QgsMapToolIdentifyFeature.__init__(self, self.canvas, self.layer)
        
        
 
    # If active layer changed, remove selection and initialize selection list.   
    def active_changed(self, layer):            
        #print("active changed : ",layer.name())
        self.nodes = []
        self.layer.removeSelection()
        if isinstance(layer, QgsVectorLayer) and layer.isSpatial():
            self.layer = layer
            self.setLayer(self.layer)

    # Convert generated path to sql for selecting by expression method *( "corridor_id" in tuple() )*
    def convertPath2SQL(self,path):
        sql_string = ' "{}" in '.format(self.field) + str(tuple(path))
        return sql_string        
        
    def selectPrevious(self):
        prevSelectExp = self.convertPath2SQL(self.nodes)
        self.layer.selectByExpression(prevSelectExp)

    def deactivate(self):
        self.layer.removeSelection()
        self.nodes = []
        self.obj.displayPath(self.nodes)

    def selectFeatures(self,path):
        self.exp = self.convertPath2SQL(path)
        self.layer.selectByExpression(self.exp)

    def degree_to_cardinal(self,d):
        
        dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        ix = round(d / (360. / len(dirs)))
        return dirs[ix % len(dirs)]

    # Creates selection tool and selects features when clicked
    # event.button() gives the event's source button (right click : 2, left click : 1)
    def canvasPressEvent(self, event):
        
        found_features = self.identify(event.x(), event.y(), [self.layer], QgsMapToolIdentify.DefaultQgsSetting)

        if not len(found_features) > 2:
            if not len(found_features) == 0:
                if event.button() == 1:
                
                    if not len(self.nodes) == 0:
                        lastSegment = self.nodes[-1]
                        
                        for i in self.layer.selectedFeatures():
                            if i[self.field] == lastSegment:
                                self.lastSegment = i
                                
                        print(lastSegment)
                    
                    if len(self.nodes) == 0:
                    
                        self.deselectedSegmentIndex = 0
                            
                        if len(found_features) == 2:
                            firstSegment = found_features[0].mFeature
                            secondSegment = found_features[1].mFeature
                            firstSegmentStr = firstSegment[self.field],self.degree_to_cardinal(180/math.pi*QgsGeometryUtils.lineAngle(firstSegment.geometry().constGet()[0][0].x(), firstSegment.geometry().constGet()[0][0].y(), firstSegment.geometry().constGet()[0][1].x(), firstSegment.geometry().constGet()[0][1].y() ))
                            secondSegmentStr = secondSegment[self.field],self.degree_to_cardinal(180/math.pi*QgsGeometryUtils.lineAngle(secondSegment.geometry().constGet()[0][0].x(), secondSegment.geometry().constGet()[0][0].y(), secondSegment.geometry().constGet()[0][1].x(), secondSegment.geometry().constGet()[0][1].y() ))
                     
                            self.obj.dlg_Selection.firstButton.setText(str(firstSegmentStr))
                            self.obj.dlg_Selection.secondButton.setText(str(secondSegmentStr))
                            self.obj.dlg_Selection.show()
                         
                            result = self.obj.dlg_Selection.exec_()
                            answer = False
                            if result:
                                answer = self.buttonValue+1
                            
                            if answer == 1 or answer == 2:
                                self.nodes.insert(self.deselectedSegmentIndex,found_features[answer-1].mFeature[self.field])
                                self.layer.selectByIds([found_features[answer-1].mFeature.id()], QgsVectorLayer.AddToSelection)

                        else:
                            self.nodes.insert(self.deselectedSegmentIndex,found_features[0].mFeature[self.field])
                            self.layer.selectByIds([found_features[0].mFeature.id()], QgsVectorLayer.AddToSelection)
                        self.deselectedSegmentIndex += 1
                        
                    # Manual Editing
                    elif self.obj.dlg.checkBoxManuel.isChecked():

                        if len(found_features) == 1:
                            for i in range(len(found_features)):
                                if found_features[i].mFeature[self.field] in self.nodes:
                                    self.layer.deselect(found_features[i].mFeature.id())
                                    for j in range(len(self.nodes)):
                                        if found_features[i].mFeature[self.field] == self.nodes[j]:
                                            self.deselectedSegmentIndex = j
                                            del self.nodes[j]
                                            break
                                else:
                                    self.nodes.insert(self.deselectedSegmentIndex,found_features[i].mFeature[self.field])
                                    self.deselectedSegmentIndex += 1
                                    self.layer.selectByIds([found_features[i].mFeature.id()], QgsVectorLayer.AddToSelection)
                            
                        elif len(found_features) == 2:
                            check = True
                            dell = False
                            firstSegment = found_features[0].mFeature
                            secondSegment = found_features[1].mFeature
                            firstSegmentStr = firstSegment[self.field],self.degree_to_cardinal(180/math.pi*QgsGeometryUtils.lineAngle(firstSegment.geometry().constGet()[0][0].x(), firstSegment.geometry().constGet()[0][0].y(), firstSegment.geometry().constGet()[0][1].x(), firstSegment.geometry().constGet()[0][1].y() ))
                            secondSegmentStr = secondSegment[self.field],self.degree_to_cardinal(180/math.pi*QgsGeometryUtils.lineAngle(secondSegment.geometry().constGet()[0][0].x(), secondSegment.geometry().constGet()[0][0].y(), secondSegment.geometry().constGet()[0][1].x(), secondSegment.geometry().constGet()[0][1].y() ))
                            try:
                                answer = int(self.obj.inputDialog(firstSegmentStr,secondSegmentStr))
                            except:
                                answer = False

                            if answer == 1:
                                
                                for j in range(len(self.nodes)):
                                    if found_features[answer-1].mFeature[self.field] == self.nodes[j]:
                                        self.layer.deselect(found_features[answer-1].mFeature.id())
                                        self.deselectedSegmentIndex = j
                                        dell = True
                                        check = False
                                        
                                    if found_features[answer].mFeature[self.field] == self.nodes[j]:
                                        self.layer.deselect(found_features[answer].mFeature.id())
                                        self.deselectedSegmentIndex = j
                                        dell = True
                                       
                                if dell == True:
                                    del self.nodes[self.deselectedSegmentIndex]
                                if check == True:
                                    self.nodes.insert(self.deselectedSegmentIndex,found_features[answer-1].mFeature[self.field])
                                    self.layer.selectByIds([found_features[answer-1].mFeature.id()], QgsVectorLayer.AddToSelection)
                                    self.deselectedSegmentIndex += 1
                                    
                            elif answer == 2:
                                for j in range(len(self.nodes)):
                                    if found_features[answer-1].mFeature[self.field] == self.nodes[j]:
                                        self.layer.deselect(found_features[answer-1].mFeature.id())
                                        self.deselectedSegmentIndex = j
                                        dell = True
                                        check = False
                                        
                                    if found_features[answer-2].mFeature[self.field] == self.nodes[j]:
                                        self.layer.deselect(found_features[answer-2].mFeature.id())
                                        self.deselectedSegmentIndex = j
                                        dell = True
                                        
                                if dell == True:
                                    del self.nodes[self.deselectedSegmentIndex]
                                    
                                if check == True:
                                    self.nodes.insert(self.deselectedSegmentIndex,found_features[answer-1].mFeature[self.field])
                                    self.layer.selectByIds([found_features[answer-1].mFeature.id()], QgsVectorLayer.AddToSelection)
                                    self.deselectedSegmentIndex += 1

                    # If only one feature found when clicked
                    elif len(found_features) == 1:

                        for i in range(len(found_features)):
                            if found_features[i].mFeature[self.field] in self.nodes:
                                self.layer.deselect(found_features[i].mFeature.id())
                                for j in range(len(self.nodes)):
                                    if found_features[i].mFeature[self.field] == self.nodes[j]:
                                        self.deselectedSegmentIndex = j
                                        del self.nodes[j]
                                        break
                            else:
                                self.nodes.insert(self.deselectedSegmentIndex,found_features[i].mFeature[self.field])
                                self.deselectedSegmentIndex += 1
                                #self.lastSegment = found_features[i]
                                self.layer.selectByIds([found_features[i].mFeature.id()], QgsVectorLayer.AddToSelection)

                    # If two features found when clicked 
                    elif len(found_features) == 2:
                        chooseSegmentList = []
                        for i in range(len(found_features)):
                            if found_features[i].mFeature[self.field] in self.nodes:
                                self.layer.deselect(found_features[i].mFeature.id())
                                for j in range(len(self.nodes)):
                                    if found_features[i].mFeature[self.field] == self.nodes[j]:
                                        self.deselectedSegmentIndex = j
                                        del self.nodes[j]
                                        break   
                            else:
                                chooseSegmentList.append(found_features[i])
                                
                        if len(chooseSegmentList) == 2:
                            lastFeaturePoint = self.lastSegment.geometry().constGet()[0][0]
                            first = chooseSegmentList[0].mFeature.geometry().constGet()[0][0]
                            second = chooseSegmentList[1].mFeature.geometry().constGet()[0][0]
                            
                            if lastFeaturePoint.distance(first) < lastFeaturePoint.distance(second):
                                self.nodes.insert(self.deselectedSegmentIndex,chooseSegmentList[0].mFeature[self.field])
                                self.layer.selectByIds([chooseSegmentList[0].mFeature.id()], QgsVectorLayer.AddToSelection)

                            else:
                                self.nodes.insert(self.deselectedSegmentIndex,chooseSegmentList[1].mFeature[self.field])
                                self.layer.selectByIds([chooseSegmentList[1].mFeature.id()], QgsVectorLayer.AddToSelection)
                            self.deselectedSegmentIndex += 1
                            
                elif event.button() == 2:   # If there is a right click (User should warn if there are twin segments )
                    if len(found_features) == 2:
                        featureOne = found_features[0].mFeature
                        featureTwo = found_features[1].mFeature
                        geomOne = featureOne.geometry()
                        geomTwo = featureTwo.geometry()
                        if geomOne.constGet()[0][0].x() == geomTwo.constGet()[0][1].x():
                            if geomOne.constGet()[0][1].y() == geomTwo.constGet()[0][0].y():
                                try:
                                    # Delete the founded one
                                    index = self.nodes.index(featureOne[self.field])
                                    self.layer.deselect(featureOne.id())
                                    del self.nodes[index]
                                    tempIndex = index
                                    # Add the other twin to selection
                                    self.nodes.insert(tempIndex,featureTwo[self.field])
                                    self.layer.selectByIds([featureTwo.id()], QgsVectorLayer.AddToSelection)
                                    
                                except ValueError:
                                    # Delete the founded one
                                    index = self.nodes.index(featureTwo[self.field])
                                    self.layer.deselect(featureTwo.id())
                                    del self.nodes[index]
                                    tempIndex = index
                                     # Add the other twin to selection
                                    self.nodes.insert(tempIndex,featureOne[self.field])
                                    self.layer.selectByIds([featureOne.id()], QgsVectorLayer.AddToSelection)

                      
        self.obj.displayPath(self.nodes)
        
