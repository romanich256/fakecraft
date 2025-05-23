def vector_add(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]

def vector_subtract(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

def vector_scale(v, scalar):
    return [v[0] * scalar, v[1] * scalar, v[2] * scalar]

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def magnitude(v):
    return (v[0]**2 + v[1]**2 + v[2]**2) ** 0.5

def normalize(v):
    mag = magnitude(v)
    if mag == 0:
        return [0, 0, 0]
    return vector_scale(v, 1/mag)

def collision_detect(pos1, size1, pos2, size2):
    return (abs(pos1[0] - pos2[0]) < (size1[0] + size2[0]) / 2 and
            abs(pos1[1] - pos2[1]) < (size1[1] + size2[1]) / 2 and
            abs(pos1[2] - pos2[2]) < (size1[2] + size2[2]) / 2)