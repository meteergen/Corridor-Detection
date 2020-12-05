<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyAlgorithm="0" maxScale="0" simplifyDrawingHints="1" minScale="100000000" labelsEnabled="1" simplifyLocal="1" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" version="3.16.0-Hannover" simplifyMaxScale="1" readOnly="0" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal fixedDuration="0" durationUnit="min" enabled="0" endExpression="" accumulate="0" startField="" mode="0" startExpression="" endField="" durationField="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 forceraster="0" symbollevels="0" type="RuleRenderer" enableorderby="1">
    <rules key="{f2d00bc5-18ac-42f3-94bf-1abf9caa3062}">
      <rule symbol="0" label="Visited" filter="&quot;visited&quot; = 1" key="{5f5f524c-46af-45a1-b59b-4d0b1299e190}"/>
      <rule symbol="1" label="Non-Visited" filter="&quot;visited&quot; is NULL" key="{47473d6d-dee5-4bf4-a6e9-c32ec430e1cd}"/>
      <rule symbol="2" filter="is_selected()" key="{36a53eee-9c7c-4484-834c-d6e1dfb18d01}"/>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" force_rhr="0" name="0" alpha="1" type="line">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,18,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.4" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="1" alpha="1" type="line">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="125,125,125,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.4" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="2" alpha="1" type="line">
        <layer enabled="1" locked="0" pass="0" class="ArrowLine">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MM" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MM" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MM" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MM" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="1" k="is_curved"/>
          <prop v="1" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@2@0" alpha="1" type="fill">
            <layer enabled="1" locked="0" pass="0" class="SimpleFill">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="24,244,0,255" k="color"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="231,113,72,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.26" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <orderby>
      <orderByClause asc="1" nullsFirst="0">is_selected()</orderByClause>
      <orderByClause asc="1" nullsFirst="1">"visited"</orderByClause>
    </orderby>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{c094df8d-f88e-442e-8e03-19595edc63dc}">
      <rule description="show id" filter="is_selected()" key="{96a2b00c-0c54-4b74-b8c7-9325b4020efa}">
        <settings calloutType="simple">
          <text-style isExpression="0" fontKerning="1" fontLetterSpacing="0" fieldName="segmentId" textOrientation="horizontal" useSubstitutions="0" textColor="0,0,0,255" textOpacity="1" fontStrikeout="0" fontItalic="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontSizeUnit="Point" previewBkgrdColor="255,255,255,255" fontFamily="MS Shell Dlg 2" namedStyle="Regular" fontWeight="50" allowHtml="0" fontUnderline="0" blendMode="0" capitalization="0" multilineHeight="1" fontWordSpacing="0" fontSize="10">
            <text-buffer bufferNoFill="1" bufferSize="1" bufferBlendMode="0" bufferSizeUnits="MM" bufferDraw="0" bufferColor="255,255,255,255" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferJoinStyle="128"/>
            <text-mask maskType="0" maskOpacity="1" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskSize="1.5" maskJoinStyle="128" maskEnabled="0" maskSizeUnits="MM" maskedSymbolLayers=""/>
            <background shapeType="0" shapeRadiiX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetY="0" shapeDraw="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeOffsetX="0" shapeSizeType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeRotationType="0" shapeJoinStyle="64" shapeSizeY="0" shapeSVGFile="" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeSizeUnit="MM" shapeRadiiUnit="MM" shapeBorderWidth="0" shapeOffsetUnit="MM" shapeBorderColor="128,128,128,255" shapeBlendMode="0">
              <symbol clip_to_extent="1" force_rhr="0" name="markerSymbol" alpha="1" type="marker">
                <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
                  <prop v="0" k="angle"/>
                  <prop v="183,72,75,255" k="color"/>
                  <prop v="1" k="horizontal_anchor_point"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="circle" k="name"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="35,35,35,255" k="outline_color"/>
                  <prop v="solid" k="outline_style"/>
                  <prop v="0" k="outline_width"/>
                  <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
                  <prop v="MM" k="outline_width_unit"/>
                  <prop v="diameter" k="scale_method"/>
                  <prop v="2" k="size"/>
                  <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
                  <prop v="MM" k="size_unit"/>
                  <prop v="1" k="vertical_anchor_point"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option name="name" type="QString" value=""/>
                      <Option name="properties"/>
                      <Option name="type" type="QString" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowDraw="0" shadowUnder="0" shadowRadius="1.5" shadowColor="0,0,0,255" shadowOffsetUnit="MM" shadowOpacity="0.7" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowOffsetDist="1" shadowOffsetAngle="135" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetGlobal="1" shadowBlendMode="6"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format placeDirectionSymbol="0" autoWrapLength="0" useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" decimals="3" multilineAlign="0" addDirectionSymbol="0" formatNumbers="0" plussign="0" wrapChar="" rightDirectionSymbol=">" reverseDirectionSymbol="0"/>
          <placement lineAnchorPercent="0.5" repeatDistance="0" maxCurvedCharAngleIn="25" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" yOffset="0" fitInPolygonOnly="0" priority="5" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidInside="0" maxCurvedCharAngleOut="-25" geometryGeneratorEnabled="0" rotationAngle="0" centroidWhole="0" lineAnchorType="0" distUnits="MM" offsetType="0" quadOffset="4" offsetUnits="MM" overrunDistanceUnit="MM" geometryGeneratorType="PointGeometry" dist="0" distMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" placementFlags="10" xOffset="0" repeatDistanceUnits="MM" geometryGenerator="" placement="2" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="LineGeometry" polygonPlacementFlags="2" overrunDistance="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0"/>
          <rendering upsidedownLabels="0" fontMaxPixelSize="10000" zIndex="0" drawLabels="1" mergeLines="0" minFeatureSize="0" fontMinPixelSize="3" displayAll="0" obstacleType="1" scaleMax="0" scaleVisibility="0" labelPerPart="0" scaleMin="0" obstacleFactor="1" obstacle="1" limitNumLabels="0" maxNumLabels="2000" fontLimitPixelSize="0"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
              <Option name="drawToAllParts" type="bool" value="false"/>
              <Option name="enabled" type="QString" value="0"/>
              <Option name="labelAnchorPoint" type="QString" value="point_on_exterior"/>
              <Option name="lineSymbol" type="QString" value="&lt;symbol clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; name=&quot;symbol&quot; alpha=&quot;1&quot; type=&quot;line&quot;>&lt;layer enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;0&quot; k=&quot;align_dash_pattern&quot;/>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;dash_pattern_offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;dash_pattern_offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option name="minLength" type="double" value="0"/>
              <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="minLengthUnit" type="QString" value="MM"/>
              <Option name="offsetFromAnchor" type="double" value="0"/>
              <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
              <Option name="offsetFromLabel" type="double" value="0"/>
              <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
    </rules>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>"roadClass"</value>
    </property>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory spacingUnitScale="3x:0,0,0,0,0,0" width="15" sizeScale="3x:0,0,0,0,0,0" rotationOffset="270" minimumSize="0" penAlpha="255" sizeType="MM" backgroundColor="#ffffff" minScaleDenominator="0" spacing="5" opacity="1" penWidth="0" enabled="0" scaleDependency="Area" scaleBasedVisibility="0" lineSizeScale="3x:0,0,0,0,0,0" backgroundAlpha="255" maxScaleDenominator="1e+08" penColor="#000000" lineSizeType="MM" barWidth="5" diagramOrientation="Up" height="15" labelPlacementMethod="XHeight" spacingUnit="MM" direction="0" showAxis="1">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" label="" field=""/>
      <axisSymbol>
        <symbol clip_to_extent="1" force_rhr="0" name="" alpha="1" type="line">
          <layer enabled="1" locked="0" pass="0" class="SimpleLine">
            <prop v="0" k="align_dash_pattern"/>
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="dash_pattern_offset"/>
            <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
            <prop v="MM" k="dash_pattern_offset_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="tweak_dash_pattern_on_corners"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" obstacle="0" dist="0" placement="2" zIndex="0" linePlacementFlags="18" showAll="1">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="segmentId">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="lengthmm">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="opSpeedKph">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="roadClass">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="spdLimKph">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="WKT">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="visited">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="segmentId" index="0"/>
    <alias name="" field="lengthmm" index="1"/>
    <alias name="" field="opSpeedKph" index="2"/>
    <alias name="" field="roadClass" index="3"/>
    <alias name="" field="spdLimKph" index="4"/>
    <alias name="" field="WKT" index="5"/>
    <alias name="" field="visited" index="6"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" expression="" field="segmentId"/>
    <default applyOnUpdate="0" expression="" field="lengthmm"/>
    <default applyOnUpdate="0" expression="" field="opSpeedKph"/>
    <default applyOnUpdate="0" expression="" field="roadClass"/>
    <default applyOnUpdate="0" expression="" field="spdLimKph"/>
    <default applyOnUpdate="0" expression="" field="WKT"/>
    <default applyOnUpdate="0" expression="" field="visited"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" exp_strength="0" field="segmentId" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" field="lengthmm" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" field="opSpeedKph" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" field="roadClass" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" field="spdLimKph" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" field="WKT" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" exp_strength="0" field="visited" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="segmentId"/>
    <constraint desc="" exp="" field="lengthmm"/>
    <constraint desc="" exp="" field="opSpeedKph"/>
    <constraint desc="" exp="" field="roadClass"/>
    <constraint desc="" exp="" field="spdLimKph"/>
    <constraint desc="" exp="" field="WKT"/>
    <constraint desc="" exp="" field="visited"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="&quot;segmentId&quot;" sortOrder="0">
    <columns>
      <column hidden="0" name="segmentId" type="field" width="-1"/>
      <column hidden="0" name="lengthmm" type="field" width="-1"/>
      <column hidden="0" name="opSpeedKph" type="field" width="-1"/>
      <column hidden="0" name="roadClass" type="field" width="-1"/>
      <column hidden="0" name="spdLimKph" type="field" width="-1"/>
      <column hidden="0" name="WKT" type="field" width="-1"/>
      <column hidden="0" name="visited" type="field" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="WKT" editable="1"/>
    <field name="lengthmm" editable="1"/>
    <field name="opSpeedKph" editable="1"/>
    <field name="roadClass" editable="1"/>
    <field name="segmentId" editable="1"/>
    <field name="spdLimKph" editable="1"/>
    <field name="visited" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="WKT"/>
    <field labelOnTop="0" name="lengthmm"/>
    <field labelOnTop="0" name="opSpeedKph"/>
    <field labelOnTop="0" name="roadClass"/>
    <field labelOnTop="0" name="segmentId"/>
    <field labelOnTop="0" name="spdLimKph"/>
    <field labelOnTop="0" name="visited"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"roadClass"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
