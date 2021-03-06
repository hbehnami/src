#ifndef TotemRP_myTotemRPOrganization_h
#define TotemRP_myTotemRPOrganization_h 

//***************************************************************************************************** Debugging
// Turns on and off the debug (Levels are: None, Error, Routine, Verbose, Trace and Debug).
// Comment the following line to turn off every kind of debug information.
// #define TotemT1Organization_DebugLevel 

//#ifdef TotemT1Organization_DebugLevel
//#include "Geometry/Totem/interface/DebugTools.h"
//#endif /* TotemT1Organization_DebugLevel */

// #define SCRIVI
//****************************************************************************************************** Includes

#include "globals.hh"
#include "SimG4CMS/PPS/interface/PPSTimingVDetectorOrganization.h"
#include "G4Step.hh"

class myPPSTimingOrganization : public PPSTimingVDetectorOrganization
{
 public:
  inline myPPSTimingOrganization();
  virtual ~myPPSTimingOrganization();

  uint32_t GetUnitID(const G4Step* aStep);
  uint32_t GetUnitID(const G4Step* aStep) const;
};


inline myPPSTimingOrganization :: myPPSTimingOrganization()
{}

#endif  //TotemRP_myTotemRPOrganization_h
