#!/usr/bin/env python3

# generate 'mandel_polydata.vtp' first !
import vtk

# source
r = vtk.vtkXMLPolyDataReader()
r.SetFileName('mandel_polydata.vtp')

# mapper
mandelMapper = vtk.vtkDataSetMapper()
mandelMapper.SetInputConnection(r.GetOutputPort())
mandelMapper.SetScalarModeToUsePointFieldData()
mandelMapper.SelectColorArray('N')
mandelMapper.SetScalarRange(0.0, 40.0)

# actor
mandelActor = vtk.vtkActor()
mandelActor.SetMapper(mandelMapper)

# renderer
ren = vtk.vtkRenderer()
ren.AddActor(mandelActor)

# window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# interactor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()

# set window size and render
renWin.SetSize(300, 300)
renWin.Render()

# start interactor loop
iren.Start()
