import os
def fcallll(fixed_distance, path):
    print("fcalll", fixed_distance, path)
    path = os.path.join("stamp_dir", path)
    os.system(f"python plot_points.py {fixed_distance} {path}")


