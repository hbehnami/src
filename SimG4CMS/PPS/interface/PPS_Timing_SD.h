/** fake sensitive detector modelled after PSimHit for a user example;
    the ORCA/CommonDet/BasicDet/interface/PSimHit.h and
    ORCA/CommonDet/PBasicDet/interface/PSimHitROUFactory.h
    are copied under Mantis/USDHitExample/test/stubs;
    the user must provide links to ORCA libraries PBasicDet, BasicDet and
    DetGeometry which must be loaded before the USDHitExample library -
    see sens.macro under Mantis/G4Application/test
 */

#ifndef PPS_PPSTimingSD_h
#define PPS_PPSTimingSD_h

/**
   In this example the TotemSensitiveDetector serves as a master for two different ExampleSD
 */

#include "SimG4Core/Application/interface/SimTrackManager.h"
#include "SimG4CMS/PPS/interface/PPS_Timing_G4Hit.h"
#include "SimG4CMS/PPS/interface/PPS_Timing_G4HitCollection.h"
#include "SimG4CMS/PPS/interface/PPSTimingVDetectorOrganization.h"

#include "SimG4Core/Notification/interface/Observer.h"
#include "SimG4Core/SensitiveDetector/interface/SensitiveTkDetector.h"
#include "SimG4Core/Notification/interface/BeginOfEvent.h"
#include "SimG4Core/Notification/interface/EndOfEvent.h"
 

#include "SimG4CMS/PPS/interface/TimingMaterialProperties.h"


#include "G4Step.hh"
#include "G4StepPoint.hh"
#include "G4Track.hh"
 
#include <string>


class G4Step;
class G4HCofThisEvent;
class TrackingSlaveSD;
//class FrameRotation;
class TotemTestHitHBNtuple;

class PPS_Timing_SD : public SensitiveTkDetector,
    public Observer<const BeginOfEvent*>,
    public Observer<const EndOfEvent*>
{
 public:    
  PPS_Timing_SD(std::string, const DDCompactView &, SensitiveDetectorCatalog &,
    edm::ParameterSet const &,const SimTrackManager*);
  virtual ~PPS_Timing_SD();
  
  void Print_Hit_Info();

  void Initialize(G4HCofThisEvent * HCE);
  virtual void EndOfEvent(G4HCofThisEvent * eventHC);
  void clear();
  void cleartrack();
  void clearTrack(G4Track * Track);


  void DrawAll();
  void PrintAll();
  
  void fillHits(edm::PSimHitContainer&, std::string use);

 private:
  virtual void clearHits();
  virtual G4bool ProcessHits(G4Step * step, G4TouchableHistory * tHistory);
  virtual uint32_t setDetUnitId(G4Step * step);
  virtual void update(const BeginOfEvent *);
  virtual void update (const ::EndOfEvent*);
    virtual void initRun();
  
  void SetNumberingScheme(PPSTimingVDetectorOrganization* scheme);

  TrackingSlaveSD* slave;
  PPSTimingVDetectorOrganization * numberingScheme;

//  int eventno;

private:
  int verbosity_;
int theMPDebug_;

  G4ThreeVector SetToLocal(G4ThreeVector globalPoint);
  void GetStepInfo(G4Step* aStep);
  G4bool HitExists();
  // void CreateNewHit();
  void ImportInfotoHit(); //added pps
  void UpdateHit();
  void StoreHit(PPS_Timing_G4Hit*);
  void ResetForNewPrimary();
  void Summarize();
  bool IsPrimary(const G4Track * track);

private:
  
  // Data relative to primary particle (the one which triggers a shower)
  // These data are common to all Hits of a given shower.
  // One shower is made of several hits which differ by the
  // unit ID (cristal/fiber/scintillator) and the Time slice ID.

  G4ThreeVector entrancePoint;
  double incidentEnergy;

  G4String name;
  G4int hcID;
  PPS_Timing_G4HitCollection* theHC; 

  PPS_Timing_G4Hit* currentHit;
  G4Track* theTrack;
  G4VPhysicalVolume* currentPV;
  unsigned int unitID;
  G4int primaryID, tSliceID;  
  //coment pps
  G4double tSlice;
TimingMaterialProperties* theMaterialProperties;

  G4StepPoint* preStepPoint; 
  G4StepPoint* postStepPoint;
  G4ThreeVector hitPoint;
   G4ThreeVector exitPoint;
  G4ThreeVector theLocalEntryPoint;
   G4ThreeVector theLocalExitPoint;

  double Pabs;
  double p_x, p_y, p_z;
  //coment pps
  double Tof;
  //coment pps 
double Eloss;	
  short ParticleType; 

  double ThetaAtEntry;
  double PhiAtEntry;

  int ParentId;
  double Vx,Vy,Vz;

  //added pps-timing
 double Globaltimehit;
double theglobaltimehit;
  //
  // Hist
  //
  static TotemTestHitHBNtuple* theNtuple;
  int eventno;
};

#endif // PPS_TotemRPSD_h
