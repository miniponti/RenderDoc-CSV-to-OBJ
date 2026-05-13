import csv

csv_file = input("Enter the CSV filename (e.g. tv.csv): ").strip()
texture_file = input("Enter texture filename (e.g. tv.png): ").strip()

vertices = []
normals = []
uvs = []
strips = []
current_strip = []

with open(csv_file, newline='') as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [h.strip() for h in reader.fieldnames]

    for row in reader:
        idx = row['IDX'].strip()

        # Primitive restart
        if idx == '--':
            if len(current_strip) >= 3:
                strips.append(current_strip)
            current_strip = []
            continue

        try:
            x = float(row['TEXCOORD0.x'])
            y = float(row['TEXCOORD0.y'])
            z = float(row['TEXCOORD0.z'])
        except ValueError:
            continue

        vertices.append((x, y, z))

        try:
            nx = float(row['TEXCOORD2.x'])
            ny = float(row['TEXCOORD2.y'])
            nz = float(row['TEXCOORD2.z'])
        except ValueError:
            nx, ny, nz = 0, 1, 0
        normals.append((nx, ny, nz))

        try:
            u = float(row['TEXCOORD8.x'])
            v = float(row['TEXCOORD8.y'])
        except ValueError:
            u, v = 0, 0
        uvs.append((u, 1.0-v))  # rotate 90°

        current_strip.append(len(vertices))  # 1-based OBJ index

    if len(current_strip) >= 3:
        strips.append(current_strip)

# Convert triangle strips → triangles with alternating winding
faces = []
for strip in strips:
    for i in range(len(strip) - 2):
        a, b, c = strip[i], strip[i+1], strip[i+2]
        if i % 2 == 0:
            faces.append((a, b, c))
        else:
            faces.append((a, c, b))

output_file = csv_file.replace('.csv', '.obj')
mtl_file = output_file.replace('.obj', '.mtl')

# Write MTL
with open(mtl_file, 'w') as f:
    f.write("newmtl mat0\n")
    f.write(f"map_Kd {texture_file}\n")

# Write OBJ
with open(output_file, 'w') as f:
    f.write(f"mtllib {mtl_file.split('/')[-1].split(chr(92))[-1]}\n")
    f.write("usemtl mat0\n")
    f.write(f"# Exported from {csv_file}\n")
    for v in vertices:
        f.write(f"v {v[0]} {v[1]} {v[2]}\n")
    for vn in normals:
        f.write(f"vn {vn[0]} {vn[1]} {vn[2]}\n")
    for vt in uvs:
        f.write(f"vt {vt[0]} {vt[1]}\n")
    for face in faces:
        a, b, c = face
        f.write(f"f {a}/{a}/{a} {b}/{b}/{b} {c}/{c}/{c}\n")

print(f"Strips: {len(strips)}, Vertices: {len(vertices)}, Faces: {len(faces)}")
print(f"Exported to {output_file}")
print(f"Material file: {mtl_file}")
