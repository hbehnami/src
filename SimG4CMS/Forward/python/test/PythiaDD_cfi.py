import FWCore.ParameterSet.Config as cms

from GeneratorInterface.Pythia6Interface.pythiaDefault_cff import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    comEnergy = cms.double(10000.0),

    PythiaParameters = cms.PSet(
        # Default (mostly empty - to keep PYTHIA default) card file
        # Name of the set is "pythiaDefault"
        pythiaDefaultBlock,
        # User cards - name is "myParameters"
        # Pythia's random generator initialization 
        myParameters = cms.vstring(),
        # This is a vector of ParameterSet names to be read, in this order
        # The first two are in the include files below
        # The last one are simply my additional parameters
        parameterSets = cms.vstring('pythiaDefault', 
            'pythiaMinBias', 
            'myParameters'),

        pythiaMinBias = cms.vstring('MSEL=0         ! User defined processes', 
            'MSUB(11)=0     ! Min bias process', 
            'MSUB(12)=0     ! Min bias process', 
            'MSUB(13)=0     ! Min bias process', 
            'MSUB(28)=0     ! Min bias process', 
            'MSUB(53)=0     ! Min bias process', 
            'MSUB(68)=0     ! Min bias process', 
            'MSUB(92)=0     ! Min bias process, single diffractive', 
            'MSUB(93)=0     ! Min bias process, single diffractive', 
            'MSUB(94)=1     ! Min bias process, double diffractive', 
            'MSUB(95)=0     ! Min bias process', 
            'MSTJ(11)=3     ! Choice of the fragmentation function', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(2)=2      ! which order running alphaS', 
            'MSTP(33)=3     ! no K factors in hard cross sections', 
            'MSTP(51)=7     ! choice of proton parton-distribution set (D=7 and means CTEQ 5L)', 
            'MSTP(52)=1     ! choice of proton pdf library (D=1 and means internal pythia one, according to MSTP(51) above',
            'MSTP(81)=1     ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model', 
            'MSTU(21)=1     ! Check on possible errors during program execution', 
            'PARP(82)=1.9409   ! pt cutoff for multiparton interactions', 
            'PARP(89)=1960. ! sqrts for which PARP82 is set', 
            'PARP(83)=0.5   ! Multiple interactions: matter distrbn parameter', 
            'PARP(84)=0.4   ! Multiple interactions: matter distribution parameter', 
            'PARP(90)=0.16  ! Multiple interactions: rescaling power', 
            'PARP(67)=2.5    ! amount of initial-state radiation', 
            'PARP(85)=1.0  ! gluon prod. mechanism in MI', 
            'PARP(86)=1.0  ! gluon prod. mechanism in MI', 
            'PARP(62)=1.25   ! ', 
            'PARP(64)=0.2    ! ', 
            'MSTP(91)=1     !', 
            'PARP(91)=2.1   ! kt distribution', 
            'PARP(93)=15.0  ! ')
    )
)

