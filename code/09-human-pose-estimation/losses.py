import torch
import torch.nn as nn
import torch.nn.functional as F

class Loss(object):
        """docstring for Loss"""
        def __init__(self, opts):
                super(Loss, self).__init__()
                self.opts = opts

        def DeepPose(self, output, target, meta=None):
                meta = (target > -0.5 + 1e-8).float().reshape(-1, self.opts.nJoints, 2) if self.opts.dataset == 'MPII' else meta[:,:,:,0]
                return F.mse_loss(output.reshape(-1, self.opts.nJoints, 2)*meta, target.reshape(-1, self.opts.nJoints, 2)*meta)
