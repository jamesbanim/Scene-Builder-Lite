# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 
# SCENE BUILDER TOOL (scene_builder_lite.py)
# Version 1.0 / 29/05/25
#
# Tool created by James Boyle (@JamesBAnim)
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Copyright (c) 2025 James Boyle
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# INSTALLATION
# Copy this file into your maya scripts directory, for example:
#
# WIN - C:/Documents and Settings/user/My Documents/maya/scripts/scene_builder_lite.py
# MACOS - /Users/user/Library/Preferences/Autodesk/maya/scripts/scene_builder_lite.py
#
# Run the tool from python command line or shelf button by 
# importing the module, and then calling the primary function:
# 
#       import scene_builder_lite
#       scene_builder_lite.run()
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# ICON
# Copy the icon JPG (scene_builder_plus_icon.jpg) to the icon folder in your maya prefs, for example:
#
# WIN - C:/Documents and Settings/user/My Documents/maya/2024/prefs/icons/scene_builder_lite_icon.jpg
# MACOS - /Users/name/Library/Preferences/Autodesk/maya/2024/prefs/icons/scene_builder_lite_icon.jpg
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# COMPATIBILITY
# Python 3
# MEL
# Maya 2022 - 2025
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# DESCRIPTION
# Scene Builder is a streamlined tool for rapid scene and shot setup in Maya. Choose from 
# a curved backdrop or load an image plane. Add a three-point light rig and a flexible camera system — 
# everything you need to jumpstart your scene and shot workflow.
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

_a='No backdrop selected.'
_Z='modelPanel'
_Y='https://www.jamesboyle.studio/scene-builder-documentation'
_X='double3'
_W='backdrops_GRP.scaleZ'
_V='backdrops_GRP.scaleY'
_U='lightRig_GRP.scaleZ'
_T='lightRig_GRP.scaleY'
_S='shotCam_GRP.scaleZ'
_R='shotCam_GRP.scaleY'
_Q='place2dTexture1.repeatV'
_P='place2dTexture1.repeatU'
_O='Add a backdrop.'
_N='Add a light rig.'
_M='Add a camera rig.'
_L=.0
_K='backdrops_GRP.rotateY'
_J='lightRig_GRP.rotateY'
_I='shotCam_GRP.rotateY'
_H='shotCam_GRP'
_G='backdrops_GRP'
_F='backdrops_GRP.scaleX'
_E='lightRig_GRP.scaleX'
_D='shotCam_GRP.scaleX'
_C='lightRig_GRP'
_B=None
_A=True
import maya.cmds as cmds,maya.OpenMaya as om,maya.mel as mel,webbrowser
__author__='James Boyle'
__version__='1.0'
title='Scene Builder'
variant='Lite'
window_name='SceneBuilderLite'
version='v1.0'
status='Release'
date='29/05/25'
window_height=538
window_width=260
content_height=505
footer_height=28
header_height=18
spacer_height=4
spacer_height_big=6
spacer_height_half=2
separator_style='in'
column_spacing=4
btn_color=.4,.4,.4
btn_width=window_width
btn_width_full=window_width
btn_width_half=window_width/2-3
btn_width_quarter=window_width/4.2
btn_width_fifth=window_width/5.4
btn_height=36
header_color_back=.345,.593,.717
header_color_mat=.2,.5,.5
header_color_light=.9,.9,.6
header_color_camera=.7,.4,.2
header_color_global=.3,.6,.5
header_color_rotate=.3,.6,.5
ramp_start=.5
ramp_end=.7
ramp_start_og_new_grad=_L
ramp_end_og_new_grad=1.
ramp_start_new_grad=_L
ramp_end_new_grad=1.
checker_color_og_1=.671,.671,.671
checker_color_og_2=.451,.451,.451
checker_color_1=.671,.671,.671
checker_color_2=.451,.451,.451
black=_L,_L,_L
curve_uv_u_zero=.4985
curve_uv_v_zero=.5022
curve_uv_u=_L,_L
curve_uv_v=_L,_L
checker_uv_og_v=15
checker_uv_og_u=15
checker_uv_u=15
checker_uv_v=15
all_lights_intensity=_L
key_light_intensity=2.5
fill_light_intensity=.8
rim_light_intensity=1.
ambient_light_intensity=.8
all_lights_intensity_subtle=_L
key_light_intensity_subtle=2.5
fill_light_intensity_subtle=.8
rim_light_intensity_subtle=1.
ambient_light_intensity_subtle=.8
dof_region=.05
all_toggle=1
key_toggle=1
fill_toggle=1
rim_toggle=1
ambient_toggle=1
object_lights=[_C]
object_backdrops=[_G]
object_camera=[_H]
zero_rotation=0
current_rotation_light=_B
current_rotation_camera=_B
current_rotation_backdrops=_B
new_rotation_light=_B
new_rotation_camera=_B
new_rotation_backdrops=_B
current_scaleX_light=_B
current_scaleY_light=_B
current_scaleZ_light=_B
current_scaleX_camera=_B
current_scaleY_camera=_B
current_scaleZ_camera=_B
current_scaleX_backdrops=_B
current_scaleY_backdrops=_B
current_scaleZ_backdrops=_B
current_scale_light=_B
current_scale_camera=_B
current_scale_backdrops=_B
new_scaleX_light=_B
new_scaleY_light=_B
new_scaleZ_light=_B
new_scaleX_camera=_B
new_scaleY_camera=_B
new_scaleZ_camera=_B
new_scaleX_backdrops=_B
new_scaleY_backdrops=_B
new_scaleZ_backdrops=_B
new_scale_light=_B
new_scale_camera=_B
new_scale_backdrops=_B
infinityFilter=cmds.itemFilter(byName='infinity*')
filtered_objects=[]
created_objects=[]
img_plane=_B
loc_cam=_B
loc_aim_cam=_B
self=_B
current_selection=_B
URL_ABOUT='https://www.linkedin.com/in/jamesboyleanimator/'
URL_TRAILER='https://vimeo.com/1085938276/207198d75a'
URL_DEMO='https://vimeo.com/1085938992/5e66e9c2e5'
URL_DOCS=_Y
URL_SUBMIT='https://jamesboylestudio.notion.site/2011447669ce803fa03bf766d691b864?pvs=105'
URL_ICONS=_Y
URL_TOOLS='https://www.jamesboyle.studio/tools-scripts'
mel_create_curve='\n    global proc create_curve(){\n        polyPlane -w 1 -h 1 -sx 10 -sy 10 -ax 0 1 0 -cuv 2 -ch 1;\n        // Result: pPlane1 polyPlane1 //\n        select -addFirst polyPlane1 ;\n        setAttr "polyPlane1.height" 1000;\n        setAttr "polyPlane1.width" 1000;\n        setAttr "polyPlane1.height" 1000;\n        setAttr "polyPlane1.subdivisionsWidth" 3;\n        setAttr "polyPlane1.subdivisionsHeight" 1;\n        DeleteHistory;\n\n        select -r pPlane1.e[1] ;\n        move -r 0 800.878724 0 ;\n        move -r -351.173951 0 0 ;\n        select -r pPlane1.e[3] ;\n        move -r -459.810498 260.222424 0 ;\n        select -r pPlane1.e[5] ;\n        move -r -439.599047 0 0 ;\n        select -r pPlane1.e[3] ;\n        move -r -32.843607 93.477958 0 ;\n        DeleteHistory;\n\n        select -r pPlane1 ;\n        select -r pPlane1.e[5] ;\n        select -tgl pPlane1.e[3] ;\n        select -tgl pPlane1.e[1] ;\n        move -r -255.707864 0 0 ;\n        select -r pPlane1 ;\n        DeleteHistory;\n\n        select -r pPlane1 ;\n        polySmooth  -mth 0 -sdt 2 -ovb 1 -ofb 3 -ofc 0 -ost 0 -ocr 0 -dv 2 -bnr 1 -c 1 -kb 1 -ksb 1 -khe 0 -kt 1 -kmb 1 -suv 1 -peh 0 -sl 1 -dpe 1 -ps 0.1 -ro 1 -ch 1 pPlane1;\n\n        manipPivot -p -303.440918 5.526568 0 ;\n        SnapToPointRelease; dR_enterForSnap;\n        manipPivot -p -4.284943 5.526568 0 ;\n        SnapToPointRelease; dR_enterForSnap; \n\n        select -r pPlane1 ;\n\n        select -r pPlane1 ;\n        select -d pPlane1.f[0:47] ;\n        select -add pPlane1.f[0:47] ;\n        select -r pPlane1.f[0] ;\n        select -tgl pPlane1.f[42] ;\n        {  string $Selection1[]; $Selection1[0] = "pPlane1.f[0]"; \n        performBestPlaneTexturing({"pPlane1.f[0]", "pPlane1.f[1]", "pPlane1.f[2]", "pPlane1.f[3]", "pPlane1.f[4]", "pPlane1.f[5]", "pPlane1.f[6]", "pPlane1.f[7]", "pPlane1.f[8]", "pPlane1.f[9]", "pPlane1.f[10]", "pPlane1.f[11]", "pPlane1.f[12]", "pPlane1.f[13]", "pPlane1.f[14]", "pPlane1.f[15]", "pPlane1.f[16]", "pPlane1.f[17]", "pPlane1.f[18]", "pPlane1.f[19]", "pPlane1.f[20]", "pPlane1.f[21]", "pPlane1.f[22]", "pPlane1.f[23]", "pPlane1.f[24]", "pPlane1.f[25]", "pPlane1.f[26]", "pPlane1.f[27]", "pPlane1.f[28]", "pPlane1.f[29]", "pPlane1.f[30]", "pPlane1.f[31]", "pPlane1.f[32]", "pPlane1.f[33]", "pPlane1.f[34]", "pPlane1.f[35]", "pPlane1.f[36]", "pPlane1.f[37]", "pPlane1.f[38]", "pPlane1.f[39]", "pPlane1.f[40]", "pPlane1.f[41]", "pPlane1.f[42]", "pPlane1.f[43]", "pPlane1.f[44]", "pPlane1.f[45]", "pPlane1.f[46]", "pPlane1.f[47]"}, $Selection1);;  };\n        polyForceUV -ni 48 pPlane1.f[47] pPlane1.f[46] pPlane1.f[45] pPlane1.f[44] pPlane1.f[43] pPlane1.f[42] pPlane1.f[41] pPlane1.f[40] pPlane1.f[39] pPlane1.f[38] pPlane1.f[37] pPlane1.f[36] pPlane1.f[35] pPlane1.f[34] pPlane1.f[33] pPlane1.f[32] pPlane1.f[31] pPlane1.f[30] pPlane1.f[29] pPlane1.f[28] pPlane1.f[27] pPlane1.f[26] pPlane1.f[25] pPlane1.f[24] pPlane1.f[23] pPlane1.f[22] pPlane1.f[21] pPlane1.f[20] pPlane1.f[19] pPlane1.f[18] pPlane1.f[17] pPlane1.f[16] pPlane1.f[15] pPlane1.f[14] pPlane1.f[13] pPlane1.f[12] pPlane1.f[11] pPlane1.f[10] pPlane1.f[9] pPlane1.f[8] pPlane1.f[7] pPlane1.f[6] pPlane1.f[5] pPlane1.f[4] pPlane1.f[3] pPlane1.f[2] pPlane1.f[1] pPlane1.f[0] pPlane1.f[0] ; \n        polyMapSew -ch 1 pPlane1.e[12:15] pPlane1.e[20:23] pPlane1.e[40:111];\n        // Result: polyMapSew1 //\n        select -d pPlane1.e[12:15] pPlane1.e[20:23] pPlane1.e[40:111] ;\n        textureWindow -edit  -checkerColorMode 0  -checkerColor1 1 1 1  -checkerColor2 0 0 0  -cgo 1  -checkerGradient1 1 1 1  -checkerGradient2 0 0 0  -checkerDensity 64  -checkerDrawTileLabels 1  -checkerTileLabelColor 1 1 1 polyTexturePlacementPanel1;\n        // Result: polyTexturePlacementPanel1 //\n        DeleteHistory;\n\n        select -r pPlane1 ;\n        DeleteHistory;\n\n        select -add pPlane1.e[12:15] pPlane1.e[20:23] pPlane1.e[40:111] ;\n        hilite pPlane1 ;\n        select -d pPlane1.e[12:15] pPlane1.e[20:23] pPlane1.e[40:111] ;\n        select -r pPlane1.f[0:47] ;\n        polyEditUV -pu 0.5 -pv 0.365082 -a -90 -rr 1 ;\n        polyMultiLayoutUV -lm 1 -sc 1 -rbf 1 -fr 1 -ps 0.2 -l 2 -gu 1 -gv 1 -psc 0 -su 1 -sv 1 -ou 0 -ov 0;\n        texOrientShells;\n        setAttr "pPlane1.uvPivot" -type double2 0.498461 0.5 ;\n        polyEditUV -u 0.133379 -v 0 ;\n\n        select -r pPlane1 ;\n        select -r pPlane1 ;\n        rotate -r -os -fo 0 -90 0 ;\n\n        rename "pPlane1" "infinityCurve_geo_01";\n        FreezeTransformations;\n        makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;\n        DeleteHistory;\n    }\ncreate_curve();\n'
mel_select_mode_all='\n    global proc select_mode_all(){\n        setSelectMode allObjects "All Objects";\n        //editMenuUpdate MayaWindow|mainEditMenu;\n        //updateSelectionModeIcons;\n        //dR_selTypeChanged("");\n    }\nselect_mode_all();\n'
mel_create_checker='\nglobal proc create_material_checker()\n{\n    shadingNode -asShader lambert;\n    sets -renderable true -noSurfaceShader true -empty -name lambert2SG;\n    connectAttr -f lambert2.outColor lambert2SG.surfaceShader;\n\n    // Proper usage of defaultNavigation for shader connections\n    defaultNavigation -createNew -destination "lambert2.color";\n    createRenderNode -allWithTexturesUp "defaultNavigation -force true -connectToExisting -source %node -destination lambert2.color" "";\n    defaultNavigation -defaultTraversal -destination "lambert2.color";\n    \n    shadingNode -asTexture checker;\n    shadingNode -asUtility place2dTexture;\n\n    connectAttr place2dTexture1.outUV checker1.uv;\n    connectAttr place2dTexture1.outUvFilterSize checker1.uvFilterSize;\n    \n    defaultNavigation -force true -connectToExisting -source checker1 -destination lambert2.color;\n    window -e -vis false createRenderNodeWindow;\n    \n    setAttr "checker1.color1" -type double3 0.55 0.55 0.55 ;\n    setAttr "checker1.color2" -type double3 0.451 0.451 0.451 ;\n    defaultNavigation -defaultTraversal -destination "checker1.uvCoord";\n\n    evalDeferred("showEditor place2dTexture1");\n    setAttr "place2dTexture1.repeatU" 15;\n    setAttr "place2dTexture1.repeatV" 15;\n    \n    select -r lambert2;\n    rename lambert2 "checker_mtl";\n    select -r checker1;\n    rename checker1 "checker_texture";\n    select -cl;\n}\n\ncreate_material_checker();\n'
mel_assign_checker='\n    global proc assign_checker(){\n        // Assign checker_mtl to selected\n        hyperShade -assign checker_mtl;\n        sets -e -forceElement lambert2SG;\n    }\nassign_checker();\n'
mel_assign_default='\n    global proc assign_lambert(){\n        // Assign lambert1 to selected\n        hyperShade -assign lambert1;\n        sets -e -forceElement lambert1SG;\n    }\nassign_lambert();\n'
mel_connect_ramp_checker='\n    global proc connect_ramp_checker(){\n        // Connect faded edges to checker\n        connectAttr -f ramp_transparency.outColor checker_mtl.transparency;\n    }\nconnect_ramp_checker();\n'
mel_connect_ramp_grid='\n    global proc connect_ramp_grid(){\n        // Connect faded edges to grid\n        connectAttr -f ramp_transparency.outColor grid_mtl.transparency;\n    }\nconnect_ramp_grid();\n'
def update_textures():
	for A in cmds.getPanel(type=_Z):
		if cmds.modelEditor(A,query=_A,activeView=_A):cmds.modelEditor(A,edit=_A,displayAppearance='smoothShaded');cmds.modelEditor(A,edit=_A,displayTextures=_A);break
def update_viewport():
	A=cmds.getPanel(withFocus=_A)
	if _Z in A:cmds.modelEditor(A,edit=_A,displayLights='all',shadows=_A,textures=_A)
def global_scale_up_all(*S):
	if not cmds.objExists(_H):om.MGlobal.displayWarning(_M)
	else:A=cmds.getAttr(_D);B=cmds.getAttr(_D);C=cmds.getAttr(_D);D=A+.2;E=B+.2;F=C+.2;cmds.setAttr(_D,D);cmds.setAttr(_R,E);cmds.setAttr(_S,F)
	if not cmds.objExists(_C):om.MGlobal.displayWarning(_N)
	else:G=cmds.getAttr(_E);H=cmds.getAttr(_E);I=cmds.getAttr(_E);J=G+.2;K=H+.2;L=I+.2;cmds.setAttr(_E,J);cmds.setAttr(_T,K);cmds.setAttr(_U,L)
	if not cmds.objExists(_G):om.MGlobal.displayWarning(_O)
	else:M=cmds.getAttr(_F);N=cmds.getAttr(_F);O=cmds.getAttr(_F);P=M+.2;Q=N+.2;R=O+.2;cmds.setAttr(_F,P);cmds.setAttr(_V,Q);cmds.setAttr(_W,R)
def global_scale_down_all(*S):
	if not cmds.objExists(_H):om.MGlobal.displayWarning(_M)
	else:A=cmds.getAttr(_D);B=cmds.getAttr(_D);C=cmds.getAttr(_D);D=A-.2;E=B-.2;F=C-.2;cmds.setAttr(_D,D);cmds.setAttr(_R,E);cmds.setAttr(_S,F)
	if not cmds.objExists(_C):om.MGlobal.displayWarning(_N)
	else:G=cmds.getAttr(_E);H=cmds.getAttr(_E);I=cmds.getAttr(_E);J=G-.2;K=H-.2;L=I-.2;cmds.setAttr(_E,J);cmds.setAttr(_T,K);cmds.setAttr(_U,L)
	if not cmds.objExists(_G):om.MGlobal.displayWarning(_O)
	else:M=cmds.getAttr(_F);N=cmds.getAttr(_F);O=cmds.getAttr(_F);P=M-.2;Q=N-.2;R=O-.2;cmds.setAttr(_F,P);cmds.setAttr(_V,Q);cmds.setAttr(_W,R)
def global_scale_up_bd(*G):
	if not cmds.objExists(_G):om.MGlobal.displayWarning(_O)
	else:A=cmds.getAttr(_F);B=cmds.getAttr(_F);C=cmds.getAttr(_F);D=A+.2;E=B+.2;F=C+.2;cmds.setAttr(_F,D);cmds.setAttr(_V,E);cmds.setAttr(_W,F)
def global_scale_down_bd(*G):
	if not cmds.objExists(_G):om.MGlobal.displayWarning(_O)
	else:A=cmds.getAttr(_F);B=cmds.getAttr(_F);C=cmds.getAttr(_F);D=A-.2;E=B-.2;F=C-.2;cmds.setAttr(_F,D);cmds.setAttr(_V,E);cmds.setAttr(_W,F)
def global_scale_up_sc(*G):
	if not cmds.objExists(_C):om.MGlobal.displayWarning(_M)
	else:A=cmds.getAttr(_D);B=cmds.getAttr(_D);C=cmds.getAttr(_D);D=A+.2;E=B+.2;F=C+.2;cmds.setAttr(_D,D);cmds.setAttr(_R,E);cmds.setAttr(_S,F)
def global_scale_down_sc(*G):
	if not cmds.objExists(_H):om.MGlobal.displayWarning(_M)
	else:A=cmds.getAttr(_D);B=cmds.getAttr(_D);C=cmds.getAttr(_D);D=A-.2;E=B-.2;F=C-.2;cmds.setAttr(_D,D);cmds.setAttr(_R,E);cmds.setAttr(_S,F)
def global_scale_up_lr(*G):
	if not cmds.objExists(_C):om.MGlobal.displayWarning(_N)
	else:A=cmds.getAttr(_E);B=cmds.getAttr(_E);C=cmds.getAttr(_E);D=A+.2;E=B+.2;F=C+.2;cmds.setAttr(_E,D);cmds.setAttr(_T,E);cmds.setAttr(_U,F)
def global_scale_down_lr(*G):
	if not cmds.objExists(_C):om.MGlobal.displayWarning(_N)
	else:A=cmds.getAttr(_E);B=cmds.getAttr(_E);C=cmds.getAttr(_E);D=A-.2;E=B-.2;F=C-.2;cmds.setAttr(_E,D);cmds.setAttr(_T,E);cmds.setAttr(_U,F)
def global_rotate_plus_45_all(*G):
	if not cmds.objExists(_H):om.MGlobal.displayWarning(_M)
	else:
		D=cmds.getAttr(_I);A=D+45;cmds.setAttr(_I,A)
		if A>315:cmds.setAttr(_I,zero_rotation)
	if not cmds.objExists(_C):om.MGlobal.displayWarning(_N)
	else:
		E=cmds.getAttr(_J);B=E+45;cmds.setAttr(_J,B)
		if B>315:cmds.setAttr(_J,zero_rotation)
	if not cmds.objExists(_G):om.MGlobal.displayWarning(_O)
	else:
		F=cmds.getAttr(_K);C=F+45;cmds.setAttr(_K,C)
		if C>315:cmds.setAttr(_K,zero_rotation)
def global_rotate_minus_45_all(*G):
	if not cmds.objExists(_H):om.MGlobal.displayWarning(_M)
	else:
		D=cmds.getAttr(_I);A=D-45;cmds.setAttr(_I,A)
		if A<-315:cmds.setAttr(_I,zero_rotation)
	if not cmds.objExists(_C):om.MGlobal.displayWarning(_N)
	else:
		E=cmds.getAttr(_J);B=E-45;cmds.setAttr(_J,B)
		if B<-315:cmds.setAttr(_J,zero_rotation)
	if not cmds.objExists(_G):om.MGlobal.displayWarning(_O)
	else:
		F=cmds.getAttr(_K);C=F-45;cmds.setAttr(_K,C)
		if C<-315:cmds.setAttr(_K,zero_rotation)
def global_rotate_plus_45_bd(*C):
	if not cmds.objExists(_G):om.MGlobal.displayWarning(_O)
	else:
		B=cmds.getAttr(_K);A=B+45;cmds.setAttr(_K,A)
		if A>315:cmds.setAttr(_K,zero_rotation)
def global_rotate_minus_45_bd(*C):
	if not cmds.objExists(_G):om.MGlobal.displayWarning(_O)
	else:
		B=cmds.getAttr(_K);A=B-45;cmds.setAttr(_K,A)
		if A<-315:cmds.setAttr(_K,zero_rotation)
def global_rotate_plus_45_sc(*C):
	if not cmds.objExists(_H):om.MGlobal.displayWarning(_M)
	else:
		B=cmds.getAttr(_I);A=B+45;cmds.setAttr(_I,A)
		if A>315:cmds.setAttr(_I,zero_rotation)
def global_rotate_minus_45_sc(*C):
	if not cmds.objExists(_H):om.MGlobal.displayWarning(_M)
	else:
		B=cmds.getAttr(_I);A=B-45;cmds.setAttr(_I,A)
		if A<-315:cmds.setAttr(_I,zero_rotation)
def global_rotate_plus_45_lr(*C):
	if not cmds.objExists(_C):om.MGlobal.displayWarning(_N)
	else:
		B=cmds.getAttr(_J);A=B+45;cmds.setAttr(_J,A)
		if A>315:cmds.setAttr(_J,zero_rotation)
def global_rotate_minus_45_lr(*C):
	if not cmds.objExists(_C):om.MGlobal.displayWarning(_N)
	else:
		B=cmds.getAttr(_J);A=B-45;cmds.setAttr(_J,A)
		if A<-315:cmds.setAttr(_J,zero_rotation)
def create_curve(*G):
	F='temp_polyPlane1';E='polyPlane1';D='temp_pPlane1';C='infinityCurve_geo_01';B='pPlane1';create_group()
	if cmds.objExists(B):cmds.rename(B,D);cmds.rename(E,F);mel.eval(mel_create_curve);A=cmds.ls(selection=_A);created_objects.extend(A);add_to_group(created_objects);cmds.rename(D,B);cmds.rename(F,E);mel.eval(mel_select_mode_all)
	elif cmds.objExists(C):cmds.select(C,replace=_A);cmds.duplicate(C)
	else:mel.eval(mel_create_curve);A=cmds.ls(selection=_A);created_objects.extend(A);add_to_group(created_objects);mel.eval(mel_select_mode_all)
def create_image_plane(*H):
	create_group();A,C=cmds.imagePlane();cmds.xform(A,scale=(25,25,25));D='imageBackground';B=1
	while cmds.objExists(f"{D}_{B}"):B+=1
	E=f"{D}_{B}";A=cmds.rename(A,E);C=cmds.listRelatives(A,shapes=_A);F=cmds.fileDialog();cmds.imagePlane(C,e=_A,fileName=F);G=cmds.ls(selection=_A);created_objects.extend(G);add_to_group(created_objects)
def create_group():
	if not cmds.objExists(_G):cmds.group(name=_G,empty=_A,world=_A)
def add_to_group(created_objects):
	A=created_objects
	for B in A:cmds.parent(B,_G);A.remove(B)
def create_checker(*A):
	if cmds.objExists('checker_mtl'):print('Checker material already exists!')
	else:mel.eval(mel_create_checker);print('Checker material created')
def assign_checker(*B):
	A=cmds.ls(selection=_A)
	if not A:om.MGlobal.displayWarning(_a)
	else:mel.eval(mel_assign_checker)
def assign_default(*B):
	A=cmds.ls(selection=_A)
	if not A:om.MGlobal.displayWarning(_a)
	else:mel.eval(mel_assign_default)
def change_checker_size_minus(checker_uv_u,checker_uv_v):A=cmds.getAttr(_P);B=cmds.getAttr(_Q);C=A+5;D=B+5;cmds.setAttr(_P,C);cmds.setAttr(_Q,D)
def change_checker_size_plus(checker_uv_u,checker_uv_v):A=cmds.getAttr(_P);B=cmds.getAttr(_Q);C=A-5;D=B-5;cmds.setAttr(_P,C);cmds.setAttr(_Q,D)
def get_assigned_material(obj):
	A=cmds.listRelatives(obj,shapes=_A)
	if not A:return
	B=cmds.listConnections(A[0],type='shadingEngine')
	if not B:return
	C=cmds.ls(cmds.listConnections(B[0]),materials=_A);return C[0]if C else _B
def create_light_rig():
	P='rotate_lightRim';O='rotate_lightFill';N='rotate_lightKey';M='aim';L='env';K='lightRig_aim_loc';J='spotLight3';I='spotLight2';H='spotLight1';G='ambientLight1';F='lightAmbient';E='lightRim';D='lightFill';C='lightKey';B='lights'
	if cmds.objExists(_C):om.MGlobal.displayWarning('A light rig already exists.');update_viewport()
	else:cmds.ambientLight();cmds.xform(G,translation=(0,350,0),rotation=(0,0,0),scale=(50,50,50));cmds.spotLight();cmds.xform(H,translation=(0,0,380),rotation=(0,0,0),scale=(50,50,50));cmds.spotLight();cmds.xform(I,translation=(380,0,0),rotation=(0,90,0),scale=(50,50,50));cmds.spotLight();cmds.xform(J,translation=(-280,0,-280),rotation=(0,-135,0),scale=(50,50,50));cmds.rename(G,F);cmds.rename(H,C);cmds.rename(I,D);cmds.rename(J,E);cmds.makeIdentity(F,apply=_A,t=_A,r=_A,s=_A);cmds.makeIdentity(C,apply=_A,t=_A,r=_A,s=_A);cmds.makeIdentity(D,apply=_A,t=_A,r=_A,s=_A);cmds.makeIdentity(E,apply=_A,t=_A,r=_A,s=_A);A=cmds.spaceLocator(name=K);A=cmds.rename(A,K);cmds.group(F,world=_A,name=L);cmds.group(C,D,E,world=_A,name=B);cmds.group(A,world=_A,name=M);cmds.group(L,B,M,name=_C);cmds.aimConstraint(A,C,offset=(0,-90,0));cmds.aimConstraint(A,D,offset=(0,-90,0));cmds.aimConstraint(A,E,offset=(0,-90,0));cmds.xform(B,translation=(0,80,0));cmds.xform(A,scale=(50,50,50));cmds.group(C,parent=B,name=N);cmds.group(D,parent=B,name=O);cmds.group(E,parent=B,name=P);cmds.xform(N,pivots=(0,0,0),worldSpace=_A);cmds.xform(O,pivots=(0,0,0),worldSpace=_A);cmds.xform(P,pivots=(0,0,0),worldSpace=_A);cmds.xform(B,pivots=(0,0,0),worldSpace=_A);cmds.xform(_C,pivots=(0,0,0),worldSpace=_A);cmds.select(deselect=_A);update_viewport();subtle_lights()
def subtle_lights():
	if not cmds.objExists(_C):create_light_rig();update_viewport()
	else:cmds.setAttr('lightAmbient.intensity',ambient_light_intensity);cmds.setAttr('lightAmbient.colorR',1.02);cmds.setAttr('lightKey.intensity',key_light_intensity);cmds.setAttr('lightKey.coneAngle',40);cmds.setAttr('lightKey.penumbraAngle',-20);cmds.setAttr('lightKey.dropoff',0);cmds.setAttr('lightKey.colorR',1.01);cmds.setAttr('lightKey.shadColorB',.1);cmds.setAttr('lightFill.intensity',fill_light_intensity);cmds.setAttr('lightFill.coneAngle',40);cmds.setAttr('lightFill.penumbraAngle',-20);cmds.setAttr('lightFill.dropoff',0);cmds.setAttr('lightFill.shadColorB',.1);cmds.setAttr('lightRim.intensity',rim_light_intensity);cmds.setAttr('lightRim.coneAngle',30);cmds.setAttr('lightRim.penumbraAngle',-20);cmds.setAttr('lightRim.dropoff',10);cmds.setAttr('lightRim.shadColorB',.1);update_viewport()
def create_camera_rig():
	C='shotCam_aim_loc';B='shotCam'
	if cmds.objExists(_H):om.MGlobal.displayWarning('A camera rig already exists.')
	else:D=cmds.camera(name=B);cmds.rename(D[0],B);A=cmds.spaceLocator(name=C);A=cmds.rename(A[0],C);cmds.group(B,A,world=_A,name=_H);cmds.xform(B,A,scale=(50,50,50));cmds.xform(A,translation=(0,0,-300));cmds.aimConstraint(A,B,offset=(0,-90,0));cmds.setAttr('shotCamShape.displayFilmGate',1);cmds.setAttr('shotCamShape.displayGateMask',1);cmds.setAttr('shotCamShape.displayGateMaskOpacity',.9);cmds.setAttr('shotCamShape.displayGateMaskColor',*black,type=_X);cmds.setAttr('shotCamShape.overscan',1);cmds.setAttr('shotCamShape.filmFit',3);cmds.camera('shotCamShape',e=_A,aspectRatio=1.78)
def dialog_info(*B):A='Close';cmds.confirmDialog(title=f"Scene Builder - by James Boyle",icon='information',message=f"""Scene Builder is a streamlined tool for rapid scene and shot setup in Maya. Choose from a curved backdrop or load an image plane. Add a three-point light rig and a flexible camera system — everything you need to jumpstart your scene and shot workflow.
 
Variant: {variant}
Version: {version}
Status: {status}
Date: {date}

© 2025 James Boyle. All rights reserved
""",button=[A],dismissString=A,parent=window_name)
def open_url_about(*A):webbrowser.open(URL_ABOUT)
def open_url_trailer(*A):webbrowser.open(URL_TRAILER)
def open_url_demo(*A):webbrowser.open(URL_DEMO)
def open_url_docs(*A):webbrowser.open(URL_DOCS)
def open_url_submit(*A):webbrowser.open(URL_SUBMIT)
def open_url_icons(*A):webbrowser.open(URL_ICONS)
def open_url_tools(*A):webbrowser.open(URL_TOOLS)
def reset_checker(self):A=checker_color_og_1;B=checker_color_og_2;cmds.setAttr('checker_texture.color1',*A,type=_X);cmds.setAttr('checker_texture.color2',*B,type=_X);C=checker_uv_og_u;D=checker_uv_og_v;cmds.setAttr(_P,C);cmds.setAttr(_Q,D)
def reset_lights(self):
	if not cmds.objExists(_C):om.MGlobal.displayWarning('No light rig exists. Add a light rig.')
	else:cmds.delete(_C);create_light_rig()
def reset_camera(self):
	if not cmds.objExists(_H):om.MGlobal.displayWarning('No camera rig exists. Add a camera rig.')
	else:cmds.delete(_H);create_camera_rig()
def run():create_ui(window_name);create_checker();cmds.select(deselect=_A)
def create_ui(window_name):
	g='left';f='globalLayout';e='cameraLayout';Z='center';O=window_name;N='rotateUVcw.png';M='rotateUVccw.png';L='Lts';K='Cam';J='UVTBAdd.png';I='UVTBRemove.png';H='boldLabelFont';D='';C='both';A='iconAndTextHorizontal'
	if cmds.window(O,exists=_A):cmds.deleteUI(O)
	a=cmds.window(O,title=f"{title} - {variant}",toolbox=_A,sizeable=False,widthHeight=(window_width+10,window_height));P=cmds.columnLayout('mainLayout',adjustableColumn=_A,columnAttach=(C,0),height=window_height+footer_height-4,width=window_width,parent=a);h=cmds.columnLayout('menuLayout',adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=P);i=cmds.scrollLayout('scrollLayout',height=window_height-footer_height,width=window_width,parent=P);E=cmds.columnLayout('contentLayout',adjustableColumn=_A,columnAttach=(C,0),height=content_height,width=window_width,parent=i);Q=cmds.columnLayout('backdropsLayout',adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=E);R=cmds.columnLayout('spacer02Layout',adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=E);S=cmds.columnLayout('materialLayout',adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=E);T=cmds.columnLayout('spacer03Layout',adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=E);U=cmds.columnLayout('lightRigLayout',adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=E);V=cmds.columnLayout('spacer05Layout',adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=E);W=cmds.columnLayout(e,adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=E);X=cmds.columnLayout('spacer06Layout',adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=E);Y=cmds.columnLayout(f,adjustableColumn=_A,columnAttach=(C,0),width=window_width,parent=E);j=cmds.columnLayout('footerLayout',adjustableColumn=_A,columnAttach=(C,0),height=footer_height,width=window_width,parent=P);b=cmds.menuBarLayout('menuBarLayout',parent=h);F=cmds.menu('menuTools',label='Tools',parent=b);cmds.menuItem(divider=_A,dividerLabel='Reset to defaults',parent=F);cmds.menuItem(label='Checker material',command=reset_checker,parent=F);cmds.menuItem(label='Light rig',command=reset_lights,parent=F);cmds.menuItem(label='Camera rig',command=reset_camera,parent=F);cmds.menuItem(divider=_A,dividerLabel='Other',parent=F);cmds.menuItem(label='Get icon',command=open_url_icons,parent=F);cmds.menuItem(label='Get more tools!',command=open_url_tools,parent=F);G=cmds.menu('menuHelp',label='Help',helpMenu=_A,parent=b);cmds.menuItem(label='About',command=dialog_info,parent=G);cmds.menuItem(label='Created by',command=open_url_about,parent=G);cmds.menuItem(label='Watch trailer',command=open_url_trailer,parent=G);cmds.menuItem(label='Watch demo',command=open_url_demo,parent=G);cmds.menuItem(label='Documentation',command=open_url_docs,parent=G);cmds.menuItem(label='Submit bug / request feature',command=open_url_submit,parent=G);cmds.text('backdropHeader',label='ADD BACKDROP',font=H,align=Z,height=header_height,backgroundColor=header_color_back,parent=Q);cmds.text(label=D,height=spacer_height,parent=Q);c=cmds.flowLayout('backdropsButtons',columnSpacing=column_spacing,width=window_width,height=btn_height,horizontal=_A,wrap=_A,parent=Q);cmds.iconTextButton('curveButton',label='Curve',style=A,image='skin.png',align=g,flat=0,width=btn_width_half-20,height=btn_height,marginWidth=8,backgroundColor=btn_color,command=create_curve,ann='Creates an infinity curve backdrop.',parent=c);cmds.iconTextButton('imageButton',label=' Add Image Plane',style=A,image='imageDisplay.png',align=g,flat=0,width=btn_width_half+20,height=btn_height,marginWidth=14,backgroundColor=btn_color,command=create_image_plane,ann='Creates an image plane for image or video reference.',parent=c);cmds.text(label=D,height=spacer_height_big,parent=R);cmds.separator(style=separator_style,parent=R);cmds.text(label=D,height=spacer_height_big,parent=R);cmds.text(label='ASSIGN MATERIAL',font=H,height=20,backgroundColor=header_color_mat,parent=S);cmds.text(label=D,height=spacer_height,parent=S);d=cmds.flowLayout('materialButtons',columnSpacing=column_spacing,width=window_width,height=btn_height,horizontal=_A,wrap=_A,parent=S);cmds.iconTextButton('checkerButton',label='Checker',style=A,flat=0,image='out_checker.png',marginWidth=13,width=btn_width_half,height=btn_height,backgroundColor=btn_color,command=assign_checker,ann='Assign the checker material',parent=d);cmds.iconTextButton('defaultLambertButton',label='Lambert1',style=A,flat=0,image='out_lambert.png',marginWidth=13,width=btn_width_half,height=btn_height,backgroundColor=btn_color,command=assign_default,ann='Assigns the default lambert1 material.',parent=d);cmds.text(label=D,height=spacer_height_big,parent=T);cmds.separator(style=separator_style,parent=T);cmds.text(label=D,height=spacer_height_big,parent=T);cmds.text(label='LIGHT RIG',font=H,height=header_height,width=btn_width_full,backgroundColor=header_color_light,parent=U);cmds.text(label=D,height=spacer_height,parent=U);k=cmds.flowLayout('lightsLayout',columnSpacing=column_spacing,width=window_width,height=btn_height,horizontal=_A,wrap=_A,parent=U);cmds.iconTextButton('addLightRigButton',label='Add lightRig and Group',style=A,flat=0,align=Z,image='ambientlight.png',marginWidth=42,width=window_width,height=btn_height,backgroundColor=btn_color,command=create_light_rig,ann='Creates a 3 point light rig and group.',parent=k);cmds.text(label=D,height=spacer_height_big,parent=V);cmds.separator(style=separator_style,parent=V);cmds.text(label=D,height=spacer_height_big,parent=V);cmds.text(label='CAMERA RIG',font=H,height=header_height,width=btn_width_full,backgroundColor=header_color_camera,parent=W);cmds.text(label=D,height=spacer_height,parent=W);l=cmds.flowLayout(e,columnSpacing=column_spacing,width=window_width,height=btn_height,horizontal=_A,wrap=_A,parent=W);cmds.iconTextButton('addCameraButton',label='Add shotCam and Group',style=A,flat=0,marginWidth=50,image='Camera.png',width=window_width,height=btn_height,backgroundColor=btn_color,command=create_camera_rig,ann='Creates a camera rig and group.',parent=l);cmds.text(label=D,height=spacer_height_big,parent=X);cmds.separator(style=separator_style,parent=X);cmds.text(label=D,height=spacer_height_big,parent=X);cmds.text(label='GLOBAL SCALE / ROTATE',font=H,align=Z,height=20,width=window_width,backgroundColor=header_color_global,parent=Y);cmds.text(label=D,height=spacer_height,parent=Y);B=cmds.flowLayout(f,columnSpacing=column_spacing,width=window_width,height=btn_height*5.49,horizontal=_A,wrap=_A,parent=Y);cmds.iconTextButton('scaleDownButton',label='Scale all down',style=A,flat=0,marginWidth=5,image=I,width=btn_width_half,height=btn_height/1.5,backgroundColor=btn_color,command=global_scale_down_all,ann='Scale all down: backdrops, light and camera rigs.',parent=B);cmds.iconTextButton('scaleUpButton',label='Scale all up',style=A,flat=0,marginWidth=5,image=J,width=btn_width_half,height=btn_height/1.5,backgroundColor=btn_color,command=global_scale_up_all,ann='Scale all up: backdrops, light and camera rigs.',parent=B);cmds.iconTextButton('scaleBDDownButton',label='Backdrop down',style=A,flat=0,marginWidth=5,image=I,width=btn_width_half,height=btn_height/1.5,backgroundColor=btn_color,command=global_scale_down_bd,ann='Scale down: backdrops.',parent=B);cmds.iconTextButton('scaleBDUpButton',label='Backdrop up',style=A,flat=0,marginWidth=5,image=J,width=btn_width_half,height=btn_height/1.5,backgroundColor=btn_color,command=global_scale_up_bd,ann='Scale up: backdrops.',parent=B);cmds.iconTextButton('scaleSCDownButton',label=K,style=A,flat=0,marginWidth=5,image=I,width=btn_width_quarter+1,height=btn_height/1.5,backgroundColor=btn_color,command=global_scale_down_sc,ann='Scale down: camera rig.',parent=B);cmds.iconTextButton('scaleSCUpButton',label=K,style=A,flat=0,marginWidth=5,image=J,width=btn_width_quarter,height=btn_height/1.5,backgroundColor=btn_color,command=global_scale_up_sc,ann='Scale up: camera rig.',parent=B);cmds.iconTextButton('scaleLRDownButton',label=L,style=A,flat=0,marginWidth=5,image=I,width=btn_width_quarter+1,height=btn_height/1.5,backgroundColor=btn_color,command=global_scale_down_lr,ann='Scale down: light rig.',parent=B);cmds.iconTextButton('scaleLRUpButton',label=L,style=A,flat=0,marginWidth=5,image=J,width=btn_width_quarter,height=btn_height/1.5,backgroundColor=btn_color,command=global_scale_up_lr,ann='Scale up: light rig.',parent=B);cmds.iconTextButton('rotateMinusButton',label='Rotate all -45',style=A,flat=0,marginWidth=5,image=M,width=btn_width_half,height=btn_height/1.5,backgroundColor=btn_color,command=global_rotate_minus_45_all,ann='Rotation all -45 degrees: backdrops, light and camera rigs.',parent=B);cmds.iconTextButton('rotatePlusButton',label='Rotate all +45',style=A,flat=0,marginWidth=5,image=N,width=btn_width_half,height=btn_height/1.5,backgroundColor=btn_color,command=global_rotate_plus_45_all,ann='Rotation all +45 degrees: backdrops, light and camera rigs.',parent=B);cmds.iconTextButton('rotateBDMinusButton',label='Backdrop -45',style=A,flat=0,marginWidth=5,image=M,width=btn_width_half,height=btn_height/1.5,backgroundColor=btn_color,command=global_rotate_minus_45_bd,ann='Rotation -45 degrees: backdrops.',parent=B);cmds.iconTextButton('rotateBDPlusButton',label='Backdrop +45',style=A,flat=0,marginWidth=5,image=N,width=btn_width_half,height=btn_height/1.5,backgroundColor=btn_color,command=global_rotate_plus_45_bd,ann='Rotation +45 degrees: backdrops.',parent=B);cmds.iconTextButton('rotateSCMinusButton',label=K,style=A,flat=0,marginWidth=5,image=M,width=btn_width_quarter+1,height=btn_height/1.5,backgroundColor=btn_color,command=global_rotate_minus_45_sc,ann='Rotation -45 degrees: camera rig.',parent=B);cmds.iconTextButton('rotateSCPlusButton',label=K,style=A,flat=0,marginWidth=5,image=N,width=btn_width_quarter,height=btn_height/1.5,backgroundColor=btn_color,command=global_rotate_plus_45_sc,ann='Rotation +45 degrees: camera rig.',parent=B);cmds.iconTextButton('rotateLRMinusButton',label=L,style=A,flat=0,marginWidth=5,image=M,width=btn_width_quarter+1,height=btn_height/1.5,backgroundColor=btn_color,command=global_rotate_minus_45_lr,ann='Rotation -45 degrees: light rig.',parent=B);cmds.iconTextButton('rotateLRPlusButton',label=L,style=A,flat=0,marginWidth=5,image=N,width=btn_width_quarter,height=btn_height/1.5,backgroundColor=btn_color,command=global_rotate_plus_45_lr,ann='Rotation +45 degrees: light rig.',parent=B);cmds.text(f"{variant}  /  {version}  /  {status}  /  {date}",font='obliqueLabelFont',height=footer_height,width=window_width,bgc=[.2,.2,.2],parent=j);cmds.showWindow(a)
if __name__=='__main__':create_ui(window_name)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# REVISIONS
#
# Revision 0: 29/05/25 : First release
