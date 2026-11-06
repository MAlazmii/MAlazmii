# Computational Studio artwork

The SVG artwork in `assets/` was created for this profile. It is conceptual artwork, not a plotted experiment or benchmark.

- `studio-header.svg`: projected toroidal wireframe with seven animated light traces. Animation is implemented inside the image and requires no scripts or external services.
- `studio-header-static.svg`: matching static variant. The profile uses it when reduced motion is requested; the animated image also includes a reduced-motion rule.
- `vision.svg`, `robotics.svg`, `simulation.svg`: matching conceptual illustrations for the profile chapters.

Palette: deep graphite, warm ivory, restrained teal, and a small warm-gold accent. The images carry their own background and work on both light and dark GitHub pages. All essential project text also appears as ordinary readable README text.

The notebook figures added to individual project READMEs are separate: those are original saved notebook outputs, with their provenance stated beside each image.

## Project images and technology marks

- `feature-matches.png` and `training-curves.png` are unchanged saved outputs from the featured computer-vision and CNN repositories. These are historical notebook results, not newly executed benchmarks. Their project READMEs document the source and limitations.
- `webots-world.jpg` is the unchanged original project screenshot linked from the robotics repository's previous README: https://github.com/MBAalotaibi/roboticSimulationDevelopedIn-Webots/assets/76629831/39da9ed0-6dc8-46b6-8bde-7a7c27342870. The controller is based on a laboratory teaching scaffold; the profile makes no exclusive authorship claim over that scaffold.
- `clustering-demo.svg` is an actual execution of the repository's unchanged k-means functions on deterministic synthetic data. It is explicitly not a coursework benchmark. Reproduce with `python examples/clustering_demo.py /path/to/Clustering-Algorithms/kmeans.py`; see the script for dependency and validation details.
- Technology logos come from [Devicon](https://github.com/devicons/devicon), under the MIT license preserved in `assets/tech/LICENSE`. The surrounding badge layout was created for this profile. These identify technologies used in the projects; they are not proficiency scores.

The live profile uses the header, project images, and technology badges. The older conceptual chapter illustrations remain in the local studio archive.

## HPC and GPU results

- `heat-diffusion.png` is the actual serial sine-mode output from [Heat MPI](https://github.com/MAlazmii/heat-mpi), comparing step 0 with step 2,000 at one fixed temperature scale. Reproduce using its `scripts/plot_field.py`; this is a numerical illustration, not a scaling benchmark.
- `gpu-reduction-a100.png` is generated from the curated [A100 measurement record](https://github.com/MAlazmii/gpu-reduction/blob/main/results/a100-validation.json) by that repository's `scripts/plot_results.py`. It shows all five repetitions and their medians/min–max ranges. The host CPU model and clock/contention controls were not captured; no peak-performance or general speedup claim is made. Both projects are independently implemented and MIT licensed.
