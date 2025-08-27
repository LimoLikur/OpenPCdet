import open3d as o3d
import numpy as np

# Ganti path ini sesuai lokasi file bin kamu
bin_path = "/home/lidar/OpenPCDet/data/nuscenes/v1.0-mini/samples/LIDAR_TOP/n008-2018-08-01-15-16-36-0400__LIDAR_TOP__1533151603547590.pcd.bin"

# Load point cloud dari file .bin (dengan 5 fitur: x, y, z, intensity, timestamp)
points = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 5)
points_xyz = points[:, :3]  # ambil hanya x, y, z

# Buat objek point cloud dari open3d
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points_xyz)

# (Opsional) Tambahkan warna berdasarkan intensity
# intensity = points[:, 3]
# intensity = (intensity - intensity.min()) / (intensity.max() - intensity.min() + 1e-5)
# pcd.colors = o3d.utility.Vector3dVector(np.tile(intensity[:, None], (1, 3)))

# Tampilkan
o3d.visualization.draw_geometries([pcd])
