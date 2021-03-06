import FWCore.ParameterSet.Config as cms

#from Configuration.TotemStandardSequences.prodT1T2Default_cfg import *

process = cms.Process("SIM")

# LoggerMax -- detail log info output including: errors.log, warnings.log, infos.log, debugs.log
# LoggerMin -- simple log info output to the standard output (e.g. screen)
process.load("Configuration.TotemCommon.LoggerMin_cfi")

# Use random number generator service
process.load("Configuration.TotemCommon.RandomNumbers_cfi")

# Specify the maximum events to simulate
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(5)
)

# input file
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:GEN.root")
)

# Smearing
process.load("IOMC.SmearingGenerator.SmearingGenerator_cfi")


# Geometry
#process.load("Configuration.TotemCommon.geometryRPT1T2CMS_cfi")
#process.load("geometryRPT1T2CMS_cfi")
process.load("Configuration.TotemCommon.geometryRP_cfi")
#process.load("Geom_RP_215_cfi")

process.XMLIdealGeometryESSource.geomXMLFiles.append('Geometry/TotemRPData/data/RP_Beta_90/RP_Dist_Beam_Cent.xml')


# Optics, needed despite the fact we do not use RPs
process.load("Configuration.TotemOpticsConfiguration.OpticsConfig_6500GeV_90_cfi")

# Looks that CMS needs it
process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
     fromDDD = cms.bool(True)
)

# Magnetic Field, by default we have 3.8T
#process.load("Configuration.StandardSequences.MagneticField_cff")

# Use particle table
process.load("SimGeneral.HepPDTESSource.pdt_cfi")

# G4 simulation & proton transport
process.load("Configuration.TotemCommon.g4SimHits_cfi")
process.g4SimHits.Generator.HepMCProductLabel = 'generator'

#process.g4SimHits.Watchers = cms.VPSet()

process.g4SimHits.UseMagneticField = False
process.g4SimHits.Physics.type = 'SimG4Core/Physics/DummyPhysics'
process.g4SimHits.Physics.DummyEMPhysics = True
process.g4SimHits.Watchers = cms.VPSet(cms.PSet(
   type       = cms.string('CheckOverlap'),
   Resolution = cms.untracked.int32(1000),  # precision, default 1000
   NodeNames  = cms.untracked.vstring('OTOTEM')
)) 



process.g4SimHits.Generator.LeaveScatteredProtons = cms.untracked.bool(True)
process.g4SimHits.Generator.LeaveOnlyScatteredProtons = cms.untracked.bool(False)
process.g4SimHits.Physics.BeamProtTransportSetup = process.BeamProtTransportSetup

# Chain of modules
process.p1 = cms.Path(process.SmearingGenerator*process.g4SimHits)

# Configure the output module (save the result in a file)
process.o1 = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *','drop *_*mix*_*_*',  'drop *_*_*TrackerHits*_*', 'drop *_*_*Muon*_*', 'drop *_*_*Ecal*_*', 'drop *_*_*Hcal*_*', 'drop *_*_*Calo*_*', 'drop *_*_*Castor*_*', 'drop *_*_*FP420SI_*', 'drop *_*_*ZDCHITS_*', 'drop *_*_*BSCHits_*', 'drop *_*_*ChamberHits_*','drop *_*_*FibreHits_*', 'drop *_*_*WedgeHits_*'),
    fileName = cms.untracked.string('file:TOTEM-SIM-forward.root')
)

process.outpath = cms.EndPath(process.o1)

# optionally dump config
#print process.dumpPython()
