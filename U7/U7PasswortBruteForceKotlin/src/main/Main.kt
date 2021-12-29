import java.io.File
fun readFileToList(file: String): List<String> = File(file).readLines()

fun main() {
    val lines = File("Wortliste_Deutsch.txt").readLines()
    for (line in lines){
        if (line.length < 10)
            println(line)
    }
}
