#ifndef T1_GAS_COLLISIONS_H
#define T1_GAS_COLLISIONS_H

/** \class CSCGasCollisions
 * Class to handle CSC gas ionization simulation during digitization.
 *
 * \author Tim Cox
 *
 * This class contains the port of the old CMSIM/ORCA Fortran routine
 * mc_clus.F, and the GEANT3 code it relied on.
 * Of course the version here is much improved :) <BR>
 */

#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
#include "SimTotem/T1Digitizer/interface/T1CrossGap.h"
#include <vector>
#include <string>

class T1GasCollisions {
 public:

  T1GasCollisions();
  virtual ~T1GasCollisions();

  void simulate(const PSimHit&, 
		std::vector<LocalPoint>& clusters, std::vector<int>& electrons );

  static const int N_GAMMA = 21;
  static const int N_ENERGY = 63;
  static const int N_ENTRIES = N_GAMMA*N_ENERGY;
  static const int MAX_STEPS = 400;

 private:
  void readCollisionTable();
  void fillCollisionsForThisGamma( float, std::vector<float>& ) const;
  float lnEnergyLoss( float, const std::vector<float>& ) const;
  double generateStep( double avCollisions ) const;
  float generateEnergyLoss( double avCollisions, 
			    double anmin, double anmax, const std::vector<float>& collisions ) const;

  void ionize( double energyTransferred, LocalPoint startHere) const;
	
  void writeSummary( int n_steps, double sum_steps, float dedx ) const;

  const std::string me;       // class name
  double gasDensity;     // Density of T1 gas mix
  // The question of what is reasonable for deCut is complex. But it seems clear that
  // this simulation is not credible if any delta electrons generated here
  // have ranges more than a few mm, or equivalently, energies above a few keV.
  // deCut = 1000 = 1 keV
  // deCut = 10000 = 10 keV
  double deCut;          // Delta electron cutoff in eV (Match GEANT!)
  double eion;           // ionization threshold (eV) (min. E for ionizatiom)
  double ework;          // effective work function (av. energy to create one ion pair)
  double clusterExtent;  // Precision of localization of ion clus. Typically 10 microns.

  std::vector<float> theGammaBins;
  std::vector<float> theEnergyBins;
  std::vector<float> theCollisionTable;

  T1CrossGap* theCrossGap; // Owned by T1GasCollisions
  bool saveGasCollisions; // Simple Configurable to flag saving info w. debugV
};

#endif
