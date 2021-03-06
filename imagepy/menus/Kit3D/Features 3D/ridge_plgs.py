from skimage.filters import frangi, sato, hessian ,meijering
from imagepy.core.engine import Filter, Simple

class Frangi(Simple):
	title = 'Frangi 3D'
	note = ['float', 'auto_msk', 'auto_snap']
	para = {'start':1, 'end':10, 'step':2, 'alpha':0.5, 'beta':0.5, 'gamma':15, 'bridges':True}

	view = [(int, 'start', (1,10), 0,  'sigma start', ''),
			(int, 'end', (1,20), 0,  'sigma start', ''),
			(int, 'step', (1,5), 0,  'sigma step', ''),
			(float, 'alpha', (0.1, 1), 1, 'alpha',''),
			(float, 'beta', (0.1, 1), 1, 'beta',''),
			(float, 'gamma', (1,30), 1, 'gamma',''),
			(bool, 'bridges', 'black ridges')]

	def run(self, ips, imgs, para = None):
		imgs[:] = frangi(imgs, range(para['start'], para['end'], para['step']), 
			alpha=para['alpha'], beta=para['beta'], gamma=para['gamma'], black_ridges=para['bridges'])
class Meijering(Simple):
	title = 'Meijering 3D'
	note = ['float', 'auto_msk', 'auto_snap']
	para = {'start':1, 'end':10, 'step':2, 'bridges':True}

	view = [(int, 'start', (1,10), 0,  'sigma start', ''),
			(int, 'end', (1,20), 0,  'sigma start', ''),
			(int, 'step', (1,5), 0,  'sigma step', ''),
			(bool, 'bridges', 'black ridges')]

	def run(self, ips, imgs, para=None):
		imgs[:] = meijering(imgs, range(para['start'], para['end'], para['step']),
			black_ridges=para['bridges'])

class Sato(Simple):
	title = 'Sato 3D'
	note = ['float', 'auto_msk', 'auto_snap']
	para = {'start':1, 'end':10, 'step':2, 'bridges':True}

	view = [(int, 'start', (1,10), 0,  'sigma start', ''),
			(int, 'end', (1,20), 0,  'sigma start', ''),
			(int, 'step', (1,5), 0,  'sigma step', ''),
			(bool, 'bridges', 'black ridges')]

	def run(self, ips, imgs, para=None):
		imgs[:] = sato(imgs, range(para['start'], para['end'], para['step']),
			black_ridges=para['bridges'])	

class Hessian(Simple):
	title = 'Hessian 3D'
	note = ['float', 'auto_msk', 'auto_snap']
	para = {'start':1, 'end':10, 'step':2, 'alpha':0.5, 'beta':0.5, 'gamma':15, 'bridges':True}

	view = [(int, 'start', (1,10), 0,  'sigma start', ''),
			(int, 'end', (1,20), 0,  'sigma start', ''),
			(int, 'step', (1,5), 0,  'sigma step', ''),
			(float, 'alpha', (0.1, 1), 1, 'alpha',''),
			(float, 'beta', (0.1, 1), 1, 'beta',''),
			(float, 'gamma', (1,30), 1, 'gamma',''),
			(bool, 'bridges', 'black ridges')]

	def run(self, ips, imgs, para = None):
		imgs[:] = hessian(imgs, range(para['start'], para['end'], para['step']), 
			alpha=para['alpha'], beta=para['beta'], gamma=para['gamma'], black_ridges=para['bridges'])

plgs = [Frangi, Meijering, Sato, Hessian]
