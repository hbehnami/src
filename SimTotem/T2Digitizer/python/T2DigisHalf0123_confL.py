import FWCore.ParameterSet.Config as cms


T2Digis = cms.EDProducer("T2DigiProducer",
   previousModule = cms.string('mix'),
   instanceLabel = cms.string('g4SimHitsTotemHitsT2Gem'),

   saveDigiVFAT=cms.bool(False),
   
   SimTrackContainerLabel = cms.InputTag("g4SimHits"),
   SimVertexContainerLabel = cms.InputTag("g4SimHits"),
   TakeOnlyPrim=cms.bool(False),
   TakeOnlySec=cms.bool(False),
        
   Misalignment = cms.PSet(                    
      simulatemisalign= cms.untracked.bool(True),
      generaterandom= cms.untracked.bool(False),
      sigmaDispl = cms.untracked.double(0.20),
      verbosity= cms.untracked.bool(False),
      inputFileNameMisal = cms.untracked.string('SimTotem/T2Digitizer/data/T2DigisHalf0123_confL.txt')
      ),


    stripHit = cms.PSet(
       # diffCoeff = cms.double(0.26),           # diffusion coefficient of driftzone
        NUMBER_OF_SIM_STEPS = cms.int32(30),    # number of uniformly distributed electron-hole pairs
        eIonE = cms.double(28.0),               # Energy to create electron/ionpair
        #gain = cms.double(8000.0),              # Gain of GEM detector
        z_max = cms.double(0.9),                # dimensions of driftzone in cm
        z_min = cms.double(0.6),
        StripWidth = cms.vdouble(0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14,0.14),
	diffCoeff = cms.vdouble(0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40),     
	gain =  cms.vdouble(10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000)
        
    ),

    padHit = cms.PSet(
        #diffCoeff = cms.double(0.26),           # diffusion coefficient of driftzone
        NUMBER_OF_SIM_STEPS = cms.int32(30),    # number of uniformly distributed electron-hole pairs
        eIonE = cms.double(28.0),               # Energy to create electron/ionpair
        #gain = cms.double(8000.0),              # Gain of GEM detector
        z_max = cms.double(0.9),                # dimensions of driftzone in cm
        z_min = cms.double(0.6),
        diffCoeff = cms.vdouble(0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40,0.40),     
	gain =  cms.vdouble(10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000)
        
    ),

                         

    stripElec = cms.PSet(
        bins = cms.vint32(40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40),
	capaNoiseFactorStrip = cms.vdouble(1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.),
	sigmaExtraNoise = cms.vint32 (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	simpleThreshold = cms.vint32 (400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400),
        UseDBInfo=cms.bool(False),
        UseCFGInfo=cms.bool(True),
        UseVFATs=cms.bool(False)
    ),

   
    
    padElec = cms.PSet(

    bins = cms.vint32(40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40),
	capaNoiseFactorPad = cms.vdouble(1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.),
	sigmaExtraNoise = cms.vint32 (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	simpleThreshold = cms.vint32 (400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400),
        UseDBInfo=cms.bool(False), # osolete, this flag is no longer supported, because of removed TotemDatabaseService module
        UseCFGInfo=cms.bool(True),
        UseVFATs=cms.bool(False)    
    )
)

