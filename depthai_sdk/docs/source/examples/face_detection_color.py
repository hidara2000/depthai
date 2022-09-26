from depthai_sdk import OakCamera

with OakCamera() as oak:
    color = oak.create_camera('color')
    nn = oak.create_nn('face-detection-retail-0004', color)
    oak.visualize([nn.out, nn.out_passthrough], scale=2/3, fps=True)
    oak.start(blocking=True)