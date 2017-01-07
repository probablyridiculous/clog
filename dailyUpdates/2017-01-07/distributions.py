###########################################
# Probability Distributions
# Sean Downes Code Log 
# 2017-01-07
# https://github.com/probablyridiculous
###########################################

import numpy as np
import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt

class Distribution(object):
	'''This an abstract class for probability distributions, instantiated with the uniform distribution.'''

	draws = 50

	def __init__(self,shape=0):
		self.name = "Uniform"
		self.shape = shape
		self.distribution = [0.01 for x in range(100)]
		self.sample = np.random.choice(range(Distribution.draws),Distribution.draws)
	
	def Histogram(self):
		'''Count the number of instances for each value drawm in the randomly generated sample dataset.'''
		return(pd.value_counts(self.sample).sort_index())

	def reSample(self,N=100):
		'''Redraw the sample dataset.'''
		self.sample = np.random.choice(range(Distribution.draws),Distribution.draws)

	def plotDistribution(self,color='g',log=True):
		'''Plot the probability distribution.'''
		plt.figure()
		if log:
		        plt.semilogy(self.distribution,color+'o:')
		else:
			plt.plot(self.distribution,color+'o:')
        	plt.title(self.name + ' Distribution with Shape Parameter: '+str(self.shape))
	        plt.xlabel('x [items]')
	        plt.ylabel('pdf(x) [likelihood of x items]')

	def plotHistogram(self,color='g'):
		'''Plot the distribution of values in the randomly generated sample dataset.'''
		plt.figure()
		self.Histogram().plot(kind='bar',color=color)
        	plt.title('Distribution of '+str(len(self.sample))+' Draws from '+self.name+' Distribution with Shape Parameter: '+str(self.shape))
        	plt.xlabel('result {broken scale}')
	        plt.ylabel('instances per result')

class Zeta(Distribution):
	'''Subclass for the family of Zeta Distributions. Also named for George Zipf.'''
	def __init__(self,shape):
		Distribution.__init__(self,shape)		
		self.name = "Zeta"
		self.distribution = ss.zipf.pmf(range(Distribution.draws),shape)
		self.sample = np.random.zipf(shape,100)	

	def reSample(self,N=100):
		self.sample = np.random.zipf(self.shape,N)

class Poisson(Distribution):
	'''Subclass for the family of Poisson Distributions.'''
	def __init__(self,shape):
                Distribution.__init__(self,shape)
                self.name = "Poisson"
                self.distribution = ss.poisson.pmf(range(Distribution.draws),shape)
		samplesize = 100
		if samplesize < 2*shape:
			samplesize = 2.1*shape 
                self.sample = np.random.poisson(shape,samplesize)

        def reSample(self,samplesize=100):
		if samplesize < 2*shape:
                        samplesize = 2.1*shape
                self.sample = np.random.poisson(shape,samplesize)
                self.sample = np.random.zipf(self.shape,N)
		
