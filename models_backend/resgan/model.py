from basicsr.archs.rrdbnet_arch import RRDBNet


class RealESRGANer(RRDBNet):
    def __init__(self):
        super().__init__(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23,
                         num_grow_ch=32, scale=4)
