package hellospark

import breeze.stats.distributions.Gamma
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.{SparkContext, SparkConf}
import org.apache.spark.mllib.linalg.distributed.RowMatrix

object CPA {

  def main(args: Array[String]) {

    val conf = new SparkConf().setMaster("local[*]").setAppName("PCAのサンプル")
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
