import FWCore.ParameterSet.Config as cms

process = cms.Process("GunVal220")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

process.load("Configuration.TotemCommon.LoggerMax_cfi")

process.load("Configuration.TotemCommon.RandomNumbers_cfi")

process.load("SimGeneral.HepPDTESSource.pdt_cfi")

# Geometry - beta* specific
process.load("Configuration.TotemCommon.geometryRP_cfi")
process.XMLIdealGeometryESSource.geomXMLFiles.append('Geometry/TotemRPData/data/RP_Beta_1535_150_out/RP_Dist_Beam_Cent.xml')

process.load("Configuration.TotemOpticsConfiguration.OpticsConfig_7000GeV_1535_cfi")

# Magnetic Field
### Full field map, static configuration for each field value
# process.load("Configuration.StandardSequences.MagneticField_20T_cff")
# process.load("Configuration.StandardSequences.MagneticField_30T_cff")
# process.load("Configuration.StandardSequences.MagneticField_35T_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
# process.load("Configuration.StandardSequences.MagneticField_40T_cff") 

# Monte Carlo gun
process.load("IOMC.FlatProtonLogKsiLogTGun.Beta1535_cfi")
process.FlatProtonLogKsiLogTGun.Verbosity = 0

# Smearing
process.load("IOMC.SmearingGenerator.SmearingGenerator_cfi")

# Oscar - G4 simulation & proton transport
process.load("Configuration.TotemCommon.g4SimHits_cfi")

# redirect the reference:
# BeamProtTransportSetup (@ Configuration.TotemCommon.g4SimHits_cfi)
# --> BeamProtTransportSetup (@ Configuration.TotemOpticsConfiguration.OpticsConfig_7000GeV_1535_cfi)
process.g4SimHits.Physics.BeamProtTransportSetup = process.BeamProtTransportSetup

process.g4SimHits.Generator.HepMCProductLabel = 'source'    # energy+vertex smearing  

process.g4SimHits.Physics.BeamProtTransportSetup.Verbosity = False

process.load("SimGeneral.MixingModule.mixNoPU_cfi")

# RP Strip digitization
process.load("SimTotem.RPDigiProducer.RPSiDetConf_cfi")

process.load("RecoTotemRP.RPClusterizer.RPClusterizationConf_cfi")
process.RPClustProd.Verbosity = 0

process.load("RecoTotemRP.RPRecoHitProducer.RPRecoHitProdConf_cfi")
process.RPHecoHitProd.Verbosity = 0

process.load("RecoTotemRP.RPSingleCandidateTrackFinder.RPSingleTrackCandFindConf_cfi")
process.RPSinglTrackCandFind.Verbosity = 0

process.load("RecoTotemRP.RPTrackCandidateCollectionFitter.RPSingleTrackCandCollFitted_cfi")
process.RPSingleTrackCandCollFit.Verbosity = 0

process.load("RecoTotemRP.RPInelasticReconstruction.Rec_beta_1535_220_cfi")
process.RP220Reconst.BeamProtTransportSetup = process.BeamProtTransportSetup
process.RP220Reconst.Verbosity = 1

process.load("TotemRPValidation.InelasticReconstructionValidation.InelasticReconstVal_1535_cfi")
process.RPInelProtRecVal.HistogramFileName = 'RPInelasticRecValHistsBeta1535.root'
process.RPInelProtRecVal.Verbosity = 0

process.HitDists = cms.EDAnalyzer("HitDistributions",
    verbosity = cms.untracked.uint32(0),
    outputFile = cms.string('hitDistributions1535.root'),
    rpList = cms.vuint32(100, 101, 102, 103, 104, 
        105, 120, 121, 122, 123, 
        124, 125, 0, 1, 2, 
        3, 4, 5, 20, 21, 
        22, 23, 24, 25)
)

process.load("TotemRPValidation.RPReconstructedTracksValidation.ReconstTracksVal_beta_1535_cfi")

process.o1 = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('inelastic_1535_smeared_sim.root')
)

process.p1 = cms.Path(process.SmearingGenerator*process.g4SimHits*process.mix*process.RPSiDetDigitizer*process.RPClustProd*process.RPHecoHitProd*process.RPSinglTrackCandFind*process.RPSingleTrackCandCollFit*process.HitDists*process.RP220Reconst*process.RPInelProtRecVal*process.RPRecTracksVal)

process.outpath = cms.EndPath(process.o1)

process.Tracer = cms.Service("Tracer")