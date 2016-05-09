package hellospark

import breeze.stats.distributions.Gamma
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.{SparkContext, SparkConf}
import org.apache.spark.mllib.linalg.distributed.RowMatrix

/**
 * Sample of dimension reduction form 20x20 to 20x5 by PCA
 * 
 * Ref:
 * https://github.com/zlpmichelle/BigRealTime/blob/9f6dab6c00e05caff0dde7773a0dbf0d11b2d7dd/src/driver.scala
 */
object PCA {

  def main(args: Array[String]) {

    val conf = new SparkConf().setMaster("local[*]").setAppName("Sample of PCA")
    val sc = new SparkContext(conf)

    val c = 20
    val gamma = new Gamma(100, 1.0 / 100)

    val vectors = (0 until c)
      .map(x => gamma.sample(c))
      .map(x => Vectors.dense(x.toArray))

    val rowRdd = sc.parallelize(vectors)
    val rowMatrix = new RowMatrix(rowRdd)
    val pcMatrix = rowMatrix.computePrincipalComponents(5)

    val toString =
      (0 until pcMatrix.numRows).map { rowNum =>
        (0 until pcMatrix.numCols).map { colNum =>
          pcMatrix(rowNum, colNum)
        }.mkString("\t")
      }.mkString("\n")

    println(toString)
  }
}
