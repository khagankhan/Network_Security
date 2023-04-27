ART = ./art.sh

JAVAC=javac
JAVA=java
CP=scroogeCoinGrader.jar:rsa.jar:algs4.jar:.

all: TestTxHandler.class

TestTxHandler.class: TestTxHandler.java
	$(JAVAC) -cp $(CP):. TestTxHandler.java

run: TestTxHandler.class
	@$(ART)
	$(JAVA) -cp $(CP):. TestTxHandler

clean:
	rm -f TestTxHandler.class
	rm -f TestIsValidTx.class
	rm -f TxHandler.class
.PHONY: all run

all: run

