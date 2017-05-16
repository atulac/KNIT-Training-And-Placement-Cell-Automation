import ODD13_14,EVEN13_14
import ODD13_14CO,EVEN13_14CO
import ODD14_15,EVEN14_15
import ODD15_16,EVEN15_16

def execute(Details,branch,Branch_Switchers,UFM):

    if branch=='CE':
        ODD13_14.execute(Details,'ODD 2013-14','Third Year CE')
        EVEN13_14.execute(Details,'EVEN 2013-14','Third Year CE')

        ODD13_14CO.execute(Details,'CO_ODD 2014-15','Third Year CE')
        EVEN13_14CO.execute(Details,'CO_EVEN 2014-15','Third Year CE')

        ODD14_15.execute(Details,'ODD 2014-15','Third Year CE',Branch_Switchers)
        EVEN14_15.execute(Details,'EVEN 2014-15','Third Year CE')

        #ODD14_15CO.execute(Details,'CO_ODD 2015-16','Third Year CE')
        #EVEN14_15CO.execute(Details,'CO_EVEN 2015-16','Third Year CE')

        ODD15_16.execute(Details,'ODD 2015-16','Third Year CE',UFM)
        EVEN15_16.execute(Details,'EVEN 2015-16','Third Year CE',UFM)


    elif branch=='CSE':

        ODD13_14.execute(Details,'ODD 2013-14','Third Year CSE')
        EVEN13_14.execute(Details,'EVEN 2013-14','Third Year CSE')

        ODD13_14CO.execute(Details,'CO_ODD 2014-15','Third Year CSE')
        EVEN13_14CO.execute(Details,'CO_EVEN 2014-15','Third Year CSE')

        ODD14_15.execute(Details,'ODD 2014-15','Third Year CSE',Branch_Switchers)
        EVEN14_15.execute(Details,'EVEN 2014-15','Third Year CSE')

        #ODD14_15CO.execute(Details,'CO_ODD 2015-16','Third Year CSE')
        #EVEN14_15CO.execute(Details,'CO_EVEN 2015-16','Third Year CSE')

        ODD15_16.execute(Details,'ODD 2015-16','Third Year CSE',UFM)
        EVEN15_16.execute(Details,'EVEN 2015-16','Third Year CSE',UFM)


    elif branch=='EE':

        ODD13_14.execute(Details,'ODD 2013-14','Third Year EE')
        EVEN13_14.execute(Details,'EVEN 2013-14','Third Year EE')

        ODD13_14CO.execute(Details,'CO_ODD 2014-15','Third Year EE')
        EVEN13_14CO.execute(Details,'CO_EVEN 2014-15','Third Year EE')

        ODD14_15.execute(Details,'ODD 2014-15','Third Year EE',Branch_Switchers)
        EVEN14_15.execute(Details,'EVEN 2014-15','Third Year EE')

        #ODD14_15CO.execute(Details,'CO_ODD 2015-16','Third Year EE')
        #EVEN14_15CO.execute(Details,'CO_EVEN 2015-16','Third Year EE')

        ODD15_16.execute(Details,'ODD 2015-16','Third Year EE',UFM)
        EVEN15_16.execute(Details,'EVEN 2015-16','Third Year EE',UFM)


    elif branch=='EL':
        ODD13_14.execute(Details,'ODD 2013-14','Third Year EL')
        EVEN13_14.execute(Details,'EVEN 2013-14','Third Year EL')

        ODD13_14CO.execute(Details,'CO_ODD 2014-15','Third Year EL')
        EVEN13_14CO.execute(Details,'CO_EVEN 2014-15','Third Year EL')

        ODD14_15.execute(Details,'ODD 2014-15','Third Year EL',Branch_Switchers)
        EVEN14_15.execute(Details,'EVEN 2014-15','Third Year EL')

        #ODD14_15CO.execute(Details,'CO_ODD 2015-16','Third Year EL')
        #EVEN14_15CO.execute(Details,'CO_EVEN 2015-16','Third Year EL')

        ODD15_16.execute(Details,'ODD 2015-16','Third Year EL',UFM)
        EVEN15_16.execute(Details,'EVEN 2015-16','Third Year EL',UFM)

    elif branch=='ME':
        ODD13_14.execute(Details,'ODD 2013-14','Third Year ME')
        EVEN13_14.execute(Details,'EVEN 2013-14','Third Year ME')

        ODD13_14CO.execute(Details,'CO_ODD 2014-15','Third Year ME')
        EVEN13_14CO.execute(Details,'CO_EVEN 2014-15','Third Year ME')

        ODD14_15.execute(Details,'ODD 2014-15','Third Year ME',Branch_Switchers)
        EVEN14_15.execute(Details,'EVEN 2014-15','Third Year ME')

        #ODD14_15CO.execute(Details,'CO_ODD 2015-16','Third Year ME')
        #EVEN14_15CO.execute(Details,'CO_EVEN 2015-16','Third Year ME')

        ODD15_16.execute(Details,'ODD 2015-16','Third Year ME',UFM)
        EVEN15_16.execute(Details,'EVEN 2015-16','Third Year ME',UFM)

    elif branch=='IT':

        ODD13_14.execute(Details,'ODD 2013-14','Third Year IT')
        EVEN13_14.execute(Details,'EVEN 2013-14','Third Year IT')

        ODD13_14CO.execute(Details,'CO_ODD 2014-15','Third Year IT')
        EVEN13_14CO.execute(Details,'CO_EVEN 2014-15','Third Year IT')

        ODD14_15.execute(Details,'ODD 2014-15','Third Year IT',Branch_Switchers)
        EVEN14_15.execute(Details,'EVEN 2014-15','Third Year IT')

        #ODD14_15CO.execute(Details,'CO_ODD 2015-16','Third Year IT')
        #EVEN14_15CO.execute(Details,'CO_EVEN 2015-16','Third Year IT')

        ODD15_16.execute(Details,'ODD 2015-16','Third Year IT',UFM)
        EVEN15_16.execute(Details,'EVEN 2015-16','Third Year IT',UFM)

    elif branch=='MCA':
        ODD13_14.execute(Details,'ODD 2013-14','Third Year MCA')
        EVEN13_14.execute(Details,'EVEN 2013-14','Third Year MCA')

        ODD13_14CO.execute(Details,'CO_ODD 2014-15','Third Year MCA')
        EVEN13_14CO.execute(Details,'CO_EVEN 2014-15','Third Year MCA')

        ODD14_15.execute(Details,'ODD 2014-15','Third Year MCA',Branch_Switchers)
        EVEN14_15.execute(Details,'EVEN 2014-15','Third Year MCA')

        #ODD14_15CO.execute(Details,'CO_ODD 2015-16','Third Year MCA')
        #EVEN14_15CO.execute(Details,'CO_EVEN 2015-16','Third Year MCA')

        ODD15_16.execute(Details,'ODD 2015-16','Third Year MCA',UFM)
        EVEN15_16.execute(Details,'EVEN 2015-16','Third Year MCA',UFM)
