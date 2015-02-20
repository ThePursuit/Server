__author__ = 'Andrea'


# Obs endast lek :)

class Player(object):

    def override(self):
        print "PLAYER override()"

    def implicit(self):
        print "PLAYER implicit()"

    def altered(self):
        print "PLAYER altered()"

class Hunted(Player):

    def override(self):
        print "Hunted override()"

    def altered(self):
        print "HUNTED, BEFORE PARENT altered()"
        super(Hunted, self).altered()
        print "HUNTED, AFTER PARENT altered()"

class Hunter(Player):

    def override(self):
        print "Hunter override()"

    def altered(self):
        print "HUNTER, BEFORE PARENT altered()"
        super(Hunter, self).altered()
        print "HUNTER, AFTER PARENT altered()"

player = Player()
hunter = Hunter()
hunted = Hunted()

player.implicit()
hunter.implicit()
hunted.implicit()

player.override()
hunter.override()
hunted.override()

player.altered()
hunter.altered()
hunted.altered()