import org.junit.jupiter.api.Test
import kotlin.test.assertEquals



internal class MainTest {
    private val testMain: Main = Main()
    private val wordsInFile = 137464
    private val fileName = "Wortliste_Deutsch.txt"

    val passString = "aBg0schn/ertem10"
    val passHex = "614267307363686e2f657274656d3130"
    val hash = "9bf2f4b49961a4a37e9517fbd54589c3f37eeb151d61971ebdcd507419d0559a"
    val passNSalt = "614267307363686E2F657274656D3130f8791d3120f151961a66c84449c3e72c"

    @Test
    internal fun test_lines_of_file() {
        assertEquals( wordsInFile, testMain.readFileToList(fileName).size, "not all lines are read")
    }

    @Test
    fun test_stringToHex() {
        var str = testMain.run {
            passString.toHex()
        }
        assertEquals(str, passHex)
    }

    @Test
    fun test_hexToHashHex() {
        assertEquals(hash, testMain.hexToHashHex(passNSalt), "Function hexToHashHex is  calculating hash incorrectly")
    }

    @Test
    fun test_hexToString(){
        assertEquals(passString, testMain.hexToString(passHex), "hex to string not correct")
    }

    @Test
    fun test_toSHA256(){
       var str =  testMain.run {
           "hello".toSHA256()
       }

        assertEquals("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", str)
    }
    @Test
    fun test_decodeHex(){
        var res = testMain.run {
            passHex.decodeHex().toHex()
        }

        assertEquals(passHex, res)
    }

    @Test
    fun test_toSHA256_byteArray(){
        var str: String =  testMain.run {
            passNSalt.decodeHex().toSHA256()
        }

        assertEquals(hash, str)
    }





}