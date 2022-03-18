__author__ = "Metehan Ergen"
__date__ = "21.02.2021"

from cProfile import label
from qgis.gui import QgsMapToolIdentify, QgsMapToolPan, QgsMapToolIdentifyFeature
from qgis.core import *
import math

class SelectTool(QgsMapToolIdentifyFeature):

    def __init__(self, iface, layer, obj):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.layer = layer
        self.nodes = []
        self.obj = obj
        self.field = ""
        self.alg_nodes = []
        self.deselectedSegmentIndex = False
        self.buttonValue = False
        QgsMapToolIdentifyFeature.__init__(self, self.canvas, self.layer)
        
    # If active layer changed, remove selection and initialize selection list.   
    def active_changed(self, layer):            
        self.nodes = []
        self.layer.removeSelection()
        if isinstance(layer, QgsVectorLayer) and layer.isSpatial():
            self.layer = layer
            self.setLayer(self.layer)

    # Convert generated path to sql for selecting by expression method *( "corridor_id" in tuple() )*
    def convertPath2SQL(self, path):
        sql_string = ' "{}" in '.format(self.field) + str(tuple(path))
        return sql_string        
        
    def selectPrevious(self):
        self.alg_nodes = []
        prevSelectExp = self.convertPath2SQL(self.nodes)
        self.layer.selectByExpression(prevSelectExp)
  

    def deactivate(self):
        self.layer.removeSelection()
        self.nodes = []
        self.alg_nodes = []
        self.obj.displayPath(self.nodes)

    def selectFeatures(self, path):
        self.exp = self.convertPath2SQL(path)
        self.layer.selectByExpression(self.exp)

    def degree_to_cardinal(self, d):
        dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        ix = round(d / (360. / len(dirs)))
        return dirs[ix % len(dirs)]

    # Creates selection tool and selects features when clicked
    # event.button() gives the event's source button (right click : 2, left click : 1)
    def canvasPressEvent(self, event):
        found_features = self.identify(event.x(), event.y(), [self.layer], QgsMapToolIdentify.DefaultQgsSetting)
        print("alg_nodes", self.alg_nodes)

        if not len(found_features) > 2:
            if not len(found_features) == 0:
                if event.button() == 1:
                
                    if not len(self.nodes) == 0:
                        lastSegment = self.nodes[-1]
                        
                        for i in self.layer.selectedFeatures():
                            # print("i", i)
                            if i[self.field] == lastSegment:
                                # print("i.field", i[self.field] )
                                self.lastSegment = i
                                
                        print(lastSegment)
                    
                    if len(self.nodes) == 0:
                    
                        self.deselectedSegmentIndex = 0
                            
                        if len(found_features) == 2:
                            firstSegment = found_features[0].mFeature
                            secondSegment = found_features[1].mFeature
                            firstSegmentStr = firstSegment[self.field],self.degree_to_cardinal(180/math.pi*QgsGeometryUtils.lineAngle(firstSegment.geometry().constGet().startPoint().x(), firstSegment.geometry().constGet().startPoint().y(), firstSegment.geometry().constGet().endPoint().x(), firstSegment.geometry().constGet().endPoint().y() ))
                            secondSegmentStr = secondSegment[self.field],self.degree_to_cardinal(180/math.pi*QgsGeometryUtils.lineAngle(secondSegment.geometry().constGet().startPoint().x(), secondSegment.geometry().constGet().startPoint().y(), secondSegment.geometry().constGet().endPoint().x(), secondSegment.geometry().constGet().endPoint().y() ))
                     
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
                        
                        if len(self.nodes)>1:
                            self.obj.runAlgorithm() 
                    # If only one feature found when clicked
                    elif len(found_features) == 1:
                    
                        for i in range(len(found_features)):
                            if found_features[i].mFeature[self.field] in self.alg_nodes:
                                index_del = self.alg_nodes.index(found_features[i].mFeature[self.field])
                                lay = [feat for feat in self.layer.getSelectedFeatures()]

                                
                                for delete in range(index_del+1, len(self.alg_nodes)):
                                    print("delete", delete)
                                    print("alg", self.alg_nodes)
                                    # idx = index_del + delete + 1
                                    seg = self.alg_nodes[delete] 

                                   
                                    print("seg", seg)
                                    for s in lay:        
                                        print(s['segmentID'], seg)                                                               
                                        if s['segmentID'] == seg:
                                           
                                            self.layer.deselect(s.id())
                                            continue

                                    if seg in self.nodes:
                                        node_index = self.nodes.index(seg)
                                        self.deselectedSegmentIndex = node_index
                                        del self.nodes[node_index]
                                        
                                
                                del self.alg_nodes[index_del+1:len(self.alg_nodes)]

                                # for j in range(len(self.nodes)):
                                #     if found_features[i].mFeature[self.field] == self.nodes[j]:
                                #         self.deselectedSegmentIndex = j
                                #         del self.nodes[j]
                                #         break
                            else:
                                self.nodes.insert(self.deselectedSegmentIndex,found_features[i].mFeature[self.field])
                                self.deselectedSegmentIndex += 1
                                #self.lastSegment = found_features[i]
                                self.layer.selectByIds([found_features[i].mFeature.id()], QgsVectorLayer.AddToSelection)
                                if len(self.nodes)>1:
                                    self.obj.runAlgorithm() 

                    # If two features found when clicked 
                    elif len(found_features) == 2:
                    
                        for i in range(len(found_features)):
                            print("foundFeatures", found_features[i].mFeature[self.field])
                        chooseSegmentList = []
                        for i in range(len(found_features)):
                            if found_features[i].mFeature[self.field] in self.alg_nodes:
                                index_del = self.alg_nodes.index(found_features[i].mFeature[self.field])
                                lay = [feat for feat in self.layer.getSelectedFeatures()]

                                
                                for delete in range(index_del+1, len(self.alg_nodes)):
                                    print("delete", delete)
                                    print("alg", self.alg_nodes)
                                    # idx = index_del + delete + 1
                                    seg = self.alg_nodes[delete] 

 
                                    
                                    print("seg", seg)
                                    for s in lay:        
                                        print(s['segmentID'], seg)                                                               
                                        if s['segmentID'] == seg:
                                           
                                            self.layer.deselect(s.id())
                                            continue

                                    if seg in self.nodes:
                                        node_index = self.nodes.index(seg)
                                        self.deselectedSegmentIndex = node_index
                                        del self.nodes[node_index]
                                         

                                
                                del self.alg_nodes[index_del+1:len(self.alg_nodes)]

                                # for j in range(len(self.nodes)):
                                #     if found_features[i].mFeature[self.field] == self.nodes[j]:
                                #         self.deselectedSegmentIndex = j
                                #         del self.nodes[j]
                                #         break   
                            else:
                                chooseSegmentList.append(found_features[i])
                                print("bp2")
                                
                        if len(chooseSegmentList) == 2:
                            lastFeaturePoint = self.lastSegment.geometry().constGet().startPoint()
                            first = chooseSegmentList[0].mFeature.geometry().constGet().startPoint()
                            second = chooseSegmentList[1].mFeature.geometry().constGet().startPoint()
                            
                            if lastFeaturePoint.distance(first) < lastFeaturePoint.distance(second):
                                print("bp3")
                                self.nodes.insert(self.deselectedSegmentIndex,chooseSegmentList[0].mFeature[self.field])
                                self.layer.selectByIds([chooseSegmentList[0].mFeature.id()], QgsVectorLayer.AddToSelection)
                                

                            else:
                                print("bp4")
                                self.nodes.insert(self.deselectedSegmentIndex,chooseSegmentList[1].mFeature[self.field])
                                self.layer.selectByIds([chooseSegmentList[1].mFeature.id()], QgsVectorLayer.AddToSelection)
                            self.deselectedSegmentIndex += 1

                            if len(self.nodes)>1:
                                self.obj.runAlgorithm()  

                       
                
                # If there is a right click (User should be warned if there are twin segments)
                elif event.button() == 2:   
                    if len(found_features) == 2:
                        if found_features[0].mFeature[self.field] in self.nodes or found_features[1].mFeature[self.field] in self.nodes:
                            featureOne = found_features[0].mFeature
                            featureTwo = found_features[1].mFeature
                            geomOne = featureOne.geometry()
                            geomTwo = featureTwo.geometry()
                            if geomOne.constGet().startPoint().x() == geomTwo.constGet().endPoint().x():
                                if geomOne.constGet().endPoint().y() == geomTwo.constGet().startPoint().y():
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
        # Only run the algorithm when at least two segments are selected.
        # if len(self.nodes)>1:
        #     self.obj.runAlgorithm() 
        #     print("Çalıştı")
        