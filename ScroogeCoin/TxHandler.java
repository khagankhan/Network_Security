import java.util.*;

public class TxHandler {
    private UTXOPool utxoPool;

    public TxHandler(UTXOPool utxoPool) {
        this.utxoPool = new UTXOPool(utxoPool);
    }

    public boolean isValidTx(Transaction tx) {
        if (tx == null) {
            throw new IllegalArgumentException("Transaction cannot be null");
        }

        HashSet<UTXO> seenUtxo = new HashSet<>();
        double inputVal = 0.0;
        double outputVal = 0.0;

        for (Transaction.Input in : tx.getInputs()) {
            UTXO ut = new UTXO(in.prevTxHash, in.outputIndex);

            if (!utxoPool.contains(ut) || seenUtxo.contains(ut)) {
                return false;
            }

            Transaction.Output output = utxoPool.getTxOutput(ut);
            if (output == null || !output.address.verifySignature(tx.getRawDataToSign(tx.getInputs().indexOf(in)), in.signature)) {
                return false;
            }

            inputVal += output.value;
            seenUtxo.add(ut);
        }

        for (Transaction.Output out : tx.getOutputs()) {
            if (out.value < 0.0) {
                return false;
            }
            outputVal += out.value;
        }

        return outputVal <= inputVal;
    }

    public Transaction[] handleTxs(Transaction[] possibleTxs) {
        if (possibleTxs == null) {
            throw new IllegalArgumentException("Possible transactions cannot be null");
        }

        HashSet<Transaction> txs = new HashSet<>(Arrays.asList(possibleTxs));
        ArrayList<Transaction> valid = new ArrayList<>();
        boolean changed;

        do {
            changed = false;
            HashSet<Transaction> toRemove = new HashSet<>();
            for (Transaction tx : txs) {
                if (isValidTx(tx)) {
                    valid.add(tx);
                    updatePool(tx);
                    toRemove.add(tx);
                    changed = true;
                }
            }
            txs.removeAll(toRemove);
        } while (changed);

        return valid.toArray(new Transaction[0]);
    }

    private void updatePool(Transaction tx) {
        if (tx == null) {
            throw new IllegalArgumentException("Transaction cannot be null");
        }

        for (Transaction.Input input : tx.getInputs()) {
            UTXO utxo = new UTXO(input.prevTxHash, input.outputIndex);
            utxoPool.removeUTXO(utxo);
        }

        int index = 0;
        for (Transaction.Output output : tx.getOutputs()) {
            UTXO utxo = new UTXO(tx.getHash(), index);
            utxoPool.addUTXO(utxo, output);
            index++;
        }
    }
}

