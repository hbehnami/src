import FWCore.ParameterSet.Config as cms

process = cms.Process("DUMP")
#process.load("Geom_RP_215_cfi")
#process.load("MYPOT_cfi")
process.load("simpletest_cfi")
#process.load("geometryRP_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger = cms.Service("MessageLogger",
                                    debugModules = cms.untracked.vstring('*'),
                                    destinations = cms.untracked.vstring('cout'),
                                    cout = cms.untracked.PSet
                                    (
    threshold = cms.untracked.string('DEBUG'),
    noLineBreaks = cms.untracked.bool(True)
    )
                                    )

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.add_(cms.ESProducer("TGeoMgrFromDdd",
        verbose = cms.untracked.bool(False),
        level   = cms.untracked.int32(14)
))

process.dump = cms.EDAnalyzer("DumpSimGeometry")

process.p = cms.Path(process.dump)


