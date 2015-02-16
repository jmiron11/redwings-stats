JC = javac
JFLAGS = -g	

.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = \
	SQLiteJDBC.java

default: classes

classes: $(CLASSES:.java=.class)

webscrape:
	python3.4 webscrape.py

clean:
	$(RM) *.class *.db