<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/studio-header-static.svg">
  <img src="assets/studio-header.svg" alt="M Alazmi — Computational Studio. From mathematical ideas to computational experiments." width="100%">
</picture>

### Hi, I'm Mohammed Alazmi.

I explore **high-performance computing, GPU programming, and scientific software**, with supporting work in machine learning and computer vision. I build small, reproducible experiments to understand numerical methods, parallel execution, and the cost of moving data.

Start with **Heat MPI**, **GPU Reduction** and **Clustering Study** below: independent projects with correctness checks, recorded validation, and reproducible results. The [MSc performance case studies](#msc-performance-case-studies) cover CPU optimisation, OpenMP tasks and MPI scaling.

**[Explore the projects ↓](#selected-projects)** &nbsp; · &nbsp; [Browse all repositories](https://github.com/MAlazmii?tab=repositories)

<p>
  <img src="assets/tech/python.svg" alt="Python" height="32">
  <img src="assets/tech/numpy.svg" alt="NumPy" height="32">
  <img src="assets/tech/tensorflow.svg" alt="TensorFlow" height="32">
  <img src="assets/tech/opencv.svg" alt="OpenCV" height="32">
  <img src="assets/tech/java.svg" alt="Java" height="32">
  <img src="assets/tech/c.svg" alt="C" height="32">
  <img src="assets/tech/jupyter.svg" alt="Jupyter" height="32">
  <img src="assets/tech/git.svg" alt="Git" height="32">
</p>

## Selected projects

<table>
<tr><td>
<sub>01 / PARALLEL COMPUTING</sub>
<h3><a href="https://github.com/MAlazmii/heat-mpi">Heat MPI — making diffusion visible</a></h3>
<p>A 2-D heat solver with a serial reference and distributed MPI implementation. Analytical checks and complete-field comparisons establish correctness; Linux validation covers Open MPI and MPICH.</p>
<p><b>C · MPI · Numerical methods</b></p>
<a href="https://github.com/MAlazmii/heat-mpi">Code, validation &amp; reproduction →</a>
<p align="center">
<a href="https://github.com/MAlazmii/heat-mpi"><img src="assets/heat-diffusion.png" alt="Actual heat solver output at the initial state and after 2,000 steps, using one temperature scale" width="760"></a><br>
<sub>Actual serial solver output. Multi-node performance has not been measured.</sub>
</p>
</td></tr>
</table>

<table>
<tr><td>
<sub>02 / GPU COMPUTING</sub>
<h3><a href="https://github.com/MAlazmii/gpu-reduction">GPU Reduction — transfers change the picture</a></h3>
<p>A C++/CUDA reduction study separating resident GPU work from transfer-inclusive time. Correctness and Compute Sanitizer checks passed on an A100; CPU builds are checked with GCC and Clang.</p>
<p><b>C++17 · CUDA · Measurement and validation</b></p>
<a href="https://github.com/MAlazmii/gpu-reduction">Code, recorded measurements &amp; methodology →</a>
<p align="center">
<a href="https://github.com/MAlazmii/gpu-reduction"><img src="assets/gpu-reduction-a100.png" alt="A100 timing chart showing five repetitions, medians and ranges for a single-thread CPU reference, resident GPU work and GPU work with transfers" width="760"></a><br>
<sub>Measured timings from one A100 run. Logarithmic scale; no general speedup claim.</sub>
</p>
</td></tr>
</table>

<table>
<tr><td>
<sub>03 / MACHINE LEARNING</sub>
<h3><a href="https://github.com/MAlazmii/clustering-study">Clustering Study — geometry and starting points matter</a></h3>
<p>An independent NumPy study of random-start k-means, k-means++ and bisecting k-means. All 225 planned fits are recorded, with numerical checks, identical-start library comparisons and repeatable Linux validation.</p>
<p><b>Python · NumPy · Reproducible experiments</b></p>
<a href="https://github.com/MAlazmii/clustering-study">Algorithms, evidence &amp; reproduction →</a>
<p align="center">
<a href="https://github.com/MAlazmii/clustering-study"><img src="assets/clustering-study-geometry.png" alt="Three generated geometries with their generating groups above and measured k-means++ assignments below, using fixed seeds" width="760"></a><br>
<sub>Actual CPU results on generated data, using fixed seeds. Colors identify groups within each panel.</sub>
</p>
<details>
<summary>See the results across every planned seed</summary>
<p align="center">
<a href="https://github.com/MAlazmii/clustering-study"><img src="assets/clustering-study-quality.png" alt="Adjusted Rand and silhouette scores for all 225 fits, with every fit, median, interquartile range and minimum–maximum range shown" width="760"></a><br>
<sub>Five dataset seeds × five initialization seeds per method and geometry. Synthetic-data measurements, not real-world accuracy estimates or confidence intervals.</sub>
</p>
</details>
</td></tr>
</table>

### MSc performance case studies

<table>
<tr><td>
<sub>04 / CPU PERFORMANCE</sub>
<h3><a href="https://github.com/MAlazmii/nbody-performance-study">N-body Performance Study</a></h3>
<p>A Cirrus optimisation study with a fresh comparison on an Apple M1. Across five runs per version, the median for 20 steps fell from 13.32 s to 0.78 s using the same input and compiler flags. The saved snapshots matched at 20 and 100 steps.</p>
<p><b>C · Profiling · Loop optimisation</b></p>
<a href="https://github.com/MAlazmii/nbody-performance-study">Case study, data &amp; method →</a>
<p align="center">
<a href="https://github.com/MAlazmii/nbody-performance-study/blob/main/figures/performance.png"><img src="assets/nbody-performance.png" alt="Six historical Cirrus runtimes and all ten fresh timing samples from the N-body solver comparison" width="760"></a><br>
<sub>The local measurements cover one solver call per process. The historical chart records the reported Cirrus stages.</sub>
</p>
</td></tr>
</table>

<table>
<tr><td>
<sub>05 / SHARED-MEMORY PARALLELISM</sub>
<h3><a href="https://github.com/MAlazmii/openmp-adaptive-quadrature">OpenMP Adaptive Quadrature</a></h3>
<p>A recursive integration study with OpenMP tasks. On the local rebuild, the median fell from 33.95 s to 9.33 s at one versus four requested threads. The estimate differed from the analytical reference by about 1.27 × 10⁻⁴.</p>
<p><b>C · OpenMP · Numerical integration</b></p>
<a href="https://github.com/MAlazmii/openmp-adaptive-quadrature">Case study, data &amp; method →</a>
<p align="center">
<a href="https://github.com/MAlazmii/openmp-adaptive-quadrature/blob/main/figures/thread-scaling.png"><img src="assets/openmp-quadrature-timings.png" alt="Historical GNU and Intel timing series and six fresh recursive solver measurements at one and four requested threads" width="760"></a><br>
<sub>The historical queue timings have unresolved source provenance. The saved queue prototype returned zero.</sub>
</p>
</td></tr>
</table>

<table>
<tr><td>
<sub>06 / DISTRIBUTED COMPUTING</sub>
<h3><a href="https://github.com/MAlazmii/mpi-sandpile-study">MPI Sandpile Study</a></h3>
<p>An ARCHER2 scaling study of a two-dimensional MPI sandpile. A temporary local build matched an independent serial reference cell for cell in all 12 checks, including runs with eight ranks.</p>
<p><b>C · MPI · Cartesian decomposition</b></p>
<a href="https://github.com/MAlazmii/mpi-sandpile-study">Case study, data &amp; method →</a>
<p align="center">
<a href="https://github.com/MAlazmii/mpi-sandpile-study/blob/main/figures/archer2-timings.png"><img src="assets/mpi-sandpile-archer2.png" alt="Fifteen archived ARCHER2 runtimes for fixed and varying grids and two node placements at 128 ranks" width="760"></a><br>
<sub>The ARCHER2 timings cover fixed iteration counts. Both node placement runs ended above the stable height.</sub>
</p>
</td></tr>
</table>

### Computer vision and robotics

<table>
<tr><td>
<sub>07 / COMPUTER VISION</sub>
<h3><a href="https://github.com/MAlazmii/2D-Convolution-SIFT-FeatureMatching">From pixels to correspondences</a></h3>
<p>Custom image filters, ORB keypoints, and SIFT/ORB matching: exploring how local image structure becomes a set of correspondences.</p>
<p><b>Python · OpenCV · NumPy</b></p>
<a href="https://github.com/MAlazmii/2D-Convolution-SIFT-FeatureMatching">Notebooks &amp; visual results →</a>
<p align="center">
<a href="https://github.com/MAlazmii/2D-Convolution-SIFT-FeatureMatching"><img src="assets/feature-matches.png" alt="Saved feature-matching output connecting corresponding points between photographs" width="600"></a>
<sub>Original saved notebook output</sub>
</p>
</td></tr>
</table>

<table>
<tr><td>
<sub>08 / ROBOTICS</sub>
<h3><a href="https://github.com/MAlazmii/roboticSimulationDevelopedIn-Webots">Finding a way through</a></h3>
<p>A Pioneer 3-DX connects sonar readings to movement through goal seeking and wall following, built on a laboratory teaching scaffold.</p>
<p><b>Java · Webots · Reactive control</b></p>
<a href="https://github.com/MAlazmii/roboticSimulationDevelopedIn-Webots">Controller &amp; setup →</a>
<p align="center">
<a href="https://github.com/MAlazmii/roboticSimulationDevelopedIn-Webots"><img src="assets/webots-world.jpg" alt="Pioneer robot and obstacles in the project's Webots arena" width="600"></a>
<sub>Original project screenshot</sub>
</p>
</td></tr>
</table>

## Also in the lab

**[Image classification with a CNN](https://github.com/MAlazmii/ImageClassificationWithCNN_)** — a TensorFlow/Keras study in grayscale image recognition, with training curves and saved evaluation outputs.

<details>
<summary>See the recorded learning curves</summary>

![Original saved CNN training curves](assets/training-curves.png)

Historical notebook output, not a new training run. [Read the experiment's scope and limitations](https://github.com/MAlazmii/ImageClassificationWithCNN_).

</details>

- **[Earlier clustering coursework](https://github.com/MAlazmii/Clustering-Algorithms)** — the original learning project, kept separate from the independently implemented Clustering Study above.
- **[Brain signal simulation](https://github.com/MAlazmii/brain_pdp)** — a C serial baseline and experimental MPI work for signal propagation through neuron-and-nerve graphs.
- **[Sales prediction prototype](https://github.com/MAlazmii/Walmart-Sales-prediction-project)** — a Flask interface connecting model inference to CSV-backed inventory charts.
- **[Geometric GUI](https://github.com/MAlazmii/GUI-Application)** — a small C# application for drawing lines and finding their intersections.

## Apps and algorithms

- **[Campus and mural map](https://github.com/MAlazmii/UOL_Map)** — a Swift coursework app exploring maps, location, and saved favourites.
- **[Wheel of Fortune](https://github.com/MAlazmii/Swift-WheelofFortune)** — a UIKit word game with phrase categories and scoring.
- **[Data cleaning](https://github.com/MAlazmii/Data_Processing)** — a JavaScript exercise in validating and normalizing CSV records.
- **[Square grouping](https://github.com/MAlazmii/Square-Grouping-problem)** — dynamic programming for partitioning a sequence into consecutive groups.

## Programming foundations

Coursework and smaller exercises are grouped by language, with original source credits and setup notes in each collection.

[Java](https://github.com/MAlazmii/java-programming) · [C](https://github.com/MAlazmii/c-programming) · [Haskell](https://github.com/MAlazmii/haskell-programming) · [Web fundamentals](https://github.com/MAlazmii/web-fundamentals) · [Swift examples](https://github.com/MAlazmii/swift_laps)

---

<p align="center"><b>Model. Validate. Measure.</b><br>Different projects, connected by curiosity about how systems work.</p>

<p align="center"><sub><a href="ARTWORK.md">Artwork &amp; image credits</a> · Animation respects reduced-motion preferences</sub></p>
