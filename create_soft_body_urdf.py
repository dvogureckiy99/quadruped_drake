from pydrake.all import *

# center_leg_link_path = "./models/mini_cheetah/meshes/"
# drake_path = getDrakePath()
# robot_description_file = "drake/" + os.path.relpath(robot_description_path, start=drake_path)
# mesh = ReadObjToTriangleSurfaceMesh(center_leg_link_path)

# deformable_body = drake.multibody.DeformableBody(mesh)
# plant = drake.multibody.MultibodyPlant(time_step=0.01)
# plant.RegisterAsSourceForSceneGraph(scene_graph)
# plant.AddDeformableBody(deformable_body)
# material = drake.multibody.DeformableContactMaterial(
#     youngs_modulus=1e6,
#     dissipation=0.01,
#     friction=0.5,
#     pressure_dependent_friction=False)
# deformable_body.SetMaterial(material)

box_geom = Box(0.01,0.004,0.014)
box_mesh = Mesh(box_geom)
volume_mesh = VolumeMesh(box_mesh)

# Create a DeformableBodyConfig object with desired material properties
material_properties = DeformableBodyConfig() 
material_properties.set_youngs_modulus(2.06e6) # in N/m^2
material_properties.set_poissons_ratio(0.3)
material_properties.set_material_model(0)
material_properties.set_mass_density(1300)
material_properties.set_stiffness_damping_coefficient(0)
material_properties.set_mass_damping_coefficient(0)

# Create a DeformableBody object from the VolumeMesh and material properties
deformable_body = DeformableBody(box_mesh, material_properties)

