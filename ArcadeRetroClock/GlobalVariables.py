#------------------------------------------------------------------------------
#                                                                            --
#      _    ____   ____    _    ____  _____    ____ _     ___   ____ _  __   --
#     / \  |  _ \ / ___|  / \  |  _ \| ____|  / ___| |   / _ \ / ___| |/ /   --
#    / _ \ | |_) | |     / _ \ | | | |  _|   | |   | |  | | | | |   | ' /    --
#   / ___ \|  _ <| |___ / ___ \| |_| | |___  | |___| |__| |_| | |___| . \    --
#  /_/   \_\_| \_\\____/_/   \_\____/|_____|  \____|_____\___/ \____|_|\_\   --
#                                                                            --
#                                                                            --
#  Global Variables                                                           --
#                                                                            --
#------------------------------------------------------------------------------
#   Version: 1.0                                                             --
#   Date:    June 11, 2020                                                   --
#   Reason:  Initial Creation                                                --
#------------------------------------------------------------------------------




MainSleep        = 0
FlashSleep       = 0
ScrollSleep      = 0
TinyClockStartHH = 0
TinyClockHours   = 0
CPUModifier      = 0
Gamma            = 0
HatWidth         = 16
HatHeight        = 16



PacDotHighScore = 0



#-----------------------------
# Outbreak Global Variables --
#-----------------------------
VirusTopSpeed     = 1
VirusBottomSpeed  = 10
VirusStartSpeed   = 20    #starting speed of the viruses
MinBright         = 100
MaxBright         = 255

OriginalMutationRate      = 200
OriginalMutationDeathRate = 5


MaxMutations              = 5    #Maximum number of mutations, if surpassed the virus dies
OriginalReplicationRate   = 2500
replicationrate           = OriginalReplicationRate
FreakoutReplicationRate   = 10    #new replication rate when a virus freaksout
MaxVirusMoves             = 50000 #after this many moves the level is over
FreakoutMoves             = 45000 #after this many moves, the viruses will replicate and mutate at a much greater rate
VirusMoves            = 0
ClumpingSpeed         = 20    #This modifies the speed of viruses that contact each other
ReplicationSpeed      = 3     #When a virus replicates, it will be a bit slower.  This number is added to current speed.
ChanceOfSpeedup       = 3     #determines how often a lone virus will spontaneously speed up
SlowTurnMinMoves      = 5     #number of moves a mutated virus moves before turning
SlowTurnMaxMoves      = 25    #number of moves a mutated virus moves before turning
MaxReplications       = 5     #Maximum number of replications, if surpassed the virus dies
InfectionChance       = 1     #Chance of one virus infecting another, lower the number greater the chance
DominanceMaxCount     = 200   #how many ticks with there being only one virus, when reached level over
VirusNameSpeedupCount = 50    #when this many virus strains are on the board, speed them up

#----------------------------
#-- PacDot                 --
#----------------------------

PacDotScore = 0
PacDotHighScore = 0



DotMatrix = [[0 for x in range(HatHeight)] for y in range(HatWidth)] 



#----------------------------
#-- DotZerk                --
#----------------------------

