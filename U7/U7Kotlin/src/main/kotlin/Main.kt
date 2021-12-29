import java.io.File
import java.security.MessageDigest

fun main() {

    Main().apply {
        val saltHex = "2c212a4a78595929e1eea5294949b0e7"
        val expectedHash = "b9a03d0233a641751ec41527c6c55326a9e23cbb07a2803c9bac9626504d7385"
//        var lines = readFileToList("src/main/resources/Wortliste_Deutsch.txt")

        var lines = readFileToList("src/main/resources/wordsAfterA.txt")

        //B
        for (wortB in lines) {
//            println(wortB)

            //C
            for ((i, ch) in wortB.withIndex()) {
                if (ch.isLowerVowel()) {
                    var tillChar: String = wortB.substring(0, i)
                    var char: Char = ch.getNumSubstitute()
                    var afterChar: String = wortB.substring(i + 1)
                    val wortC = tillChar + char + afterChar
//                    println(" " + wortC)

                    //D
                    for ((i1, ch1) in wortC.withIndex()) {
                        if (ch1.isLowerVowel()) {
                            var tillChar1: String = wortC.substring(0, i1)
                            var char1: Char = ch1.getSymbolSubstitute()
                            var afterChar1: String = wortC.substring(i1 + 1)
                            val wortD = tillChar1 + char1 + afterChar1
//                            println("  " + wortD)

                            //E
                            for (n in 1..20) {
                                val wortE = wortD + n
//                                println("   " + wortE)

//                                //HASH
                                var passString = wortE
                                val passNsaltHex = passString.toHex() + saltHex
                                val actualHash = passNsaltHex.decodeHex().toSHA256()
                                if (actualHash == expectedHash) {
                                    println(wortE)
                                    println(actualHash)
                                }
//                                break //E
                            }
//                            break //D
                        }
                    }
//                    break //C
                }
            }
//            break //B
        }


//        val fileName = "src/main/resources/wordsAfterA.txt"
//        val myfile = File(fileName)
//        myfile.printWriter().use { out ->
//            for (word in lines) {
//                var lowerWord = word.lowercase()
//                val firstUp = "${lowerWord[0].uppercase()}${lowerWord.substring(1)}"
//                val secondUp = "${lowerWord[0]}${lowerWord[1].uppercase()}${lowerWord.substring(2)}"
//
//                out.println(firstUp)
//                out.println(secondUp)
//            }
//        }


    }


}


class Main {

    fun Char.isLowerVowel(): Boolean {
        return (this == 'a' || this == 'e' || this == 'i' || this == 'o' || this == 'u')
    }

    fun Char.getNumSubstitute(): Char {
        return when (this) {
            'a' -> '9'
            'e' -> '1'
            'i' -> '5'
            'o' -> '8'
            else -> '5' //case u
        }
    }

    fun Char.getSymbolSubstitute(): Char {
        return when (this) {
            'a' -> '('
            'e' -> ':'
            'i' -> '$'
            'o' -> '_'
            else -> '|' //case u
        }
    }

    fun readFileToList(file: String): List<String> = File(file).readLines()

    fun String.toHex(): String = this.toByteArray().toHex()

    fun String.toSHA256(): String {
        val bytes = MessageDigest.getInstance("SHA-256").digest(this.toByteArray())
        return bytes.toHex()
    }

    fun String.decodeHex(): ByteArray {
        check(length % 2 == 0) { "Must have an even length" }

        return ByteArray(length / 2) {
            Integer.parseInt(this, it * 2, (it + 1) * 2, 16).toByte()
        }
    }

    fun ByteArray.toHex(): String {
        return joinToString("") { "%02x".format(it) }
    }

    fun ByteArray.toSHA256(): String {
        val bytes = MessageDigest.getInstance("SHA-256").digest(this)
        return bytes.toHex()
    }
}


/*
* Task_ID (max. 3 chars): 7A
Matrikelnummer (6 or 7 chars): 1238240
Salt:
2c212a4a78595929e1eea5294949b0e7
Password Hash:
b9a03d0233a641751ec41527c6c55326a9e23cbb07a2803c9bac9626504d7385
Substitutionen:
a durch ( oder 9
e durch : oder 1
i durch $ oder 5
o durch _ oder 8
u durch | oder 5
OK*/