#!/usr/bin/env python3
"""Render an actual k-means run on synthetic 2D data; no network access.

Usage:
  python clustering_demo.py /path/to/Clustering-Algorithms/kmeans.py

Dependencies: numpy, matplotlib, scikit-learn (imported by original source).
Source: https://github.com/MAlazmii/Clustering-Algorithms/blob/main/kmeans.py
Reviewed Git blob: e9171962fdadca37e7be5587e908b12b1ccb1e37
The original algorithm is imported unchanged. Only use a trusted source file.
"""

import argparse
import hashlib
import importlib.util
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/github-profile-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Local, reviewed kmeans.py")
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "assets/clustering-demo.svg")
    args = parser.parse_args()
    source = args.source.resolve()
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    spec = importlib.util.spec_from_file_location("reviewed_kmeans", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    rng = np.random.default_rng(42)
    centers = np.array([[-3.2, -1.6], [0.0, 2.8], [3.3, -1.0]])
    points = np.concatenate([rng.normal(c, [0.72, 0.65], size=(90, 2))
                             for c in centers])
    rng.shuffle(points)
    labels, centroids = module.clustername(points, 3, maxIter=100)
    assert np.isfinite(centroids).all(), "Non-finite centroids"
    assert len(np.unique(labels)) == 3, "Expected three occupied clusters"
    expected = np.argmin(((points[:, None, :] - centroids[None, :, :]) ** 2).sum(2), axis=1)
    assert np.array_equal(labels, expected), "Assignments differ from nearest centroids"
    for i in range(3):
        assert np.allclose(centroids[i], points[labels == i].mean(0))

    # Order only the presentation colors; original assignments remain unchanged.
    order = np.argsort(centroids[:, 0])
    colors = ["#52ddcb", "#a48bff", "#ffbd76"]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "svg.fonttype": "path", "svg.hashsalt": "malazmii-clustering-demo"})
    bg, muted, ink = "#0b1220", "#a9b8ca", "#edf5ff"
    fig, ax = plt.subplots(figsize=(12, 7), facecolor=bg)
    fig.subplots_adjust(left=0.10, right=0.97, top=0.78, bottom=0.24)
    ax.set_facecolor(bg)
    for j, i in enumerate(order):
        xy = points[labels == i]
        ax.scatter(xy[:, 0], xy[:, 1], s=30, c=colors[j], alpha=0.82,
                   linewidths=0, label=f"Cluster {j + 1} · {len(xy)} points", zorder=3)
    ax.scatter(centroids[:, 0], centroids[:, 1], marker="X", s=200,
               c="white", edgecolors=bg, linewidths=1.7, label="Learned centroid", zorder=5)
    ax.set_xlabel("Feature 1 (arbitrary units)", color=muted, labelpad=10)
    ax.set_ylabel("Feature 2 (arbitrary units)", color=muted, labelpad=10)
    ax.tick_params(colors=muted, length=0, pad=8)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(color="#223047", linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)
    ax.set_aspect("equal", adjustable="datalim")
    fig.text(0.10, 0.94, "ALGORITHMS / NUMPY", color=colors[0], fontsize=11, weight="bold")
    fig.text(0.10, 0.875, "Finding structure in the data", color=ink, fontsize=27, weight="bold")
    fig.text(0.10, 0.825, "Actual k-means assignments · 270 generated points · k = 3", color=muted, fontsize=12)
    handles, names = ax.get_legend_handles_labels()
    fig.legend(handles, names, loc="lower center", bbox_to_anchor=(0.54, 0.105),
               ncol=4, frameon=False, labelcolor=ink, fontsize=10, handletextpad=0.4)
    fig.text(0.10, 0.073, "Synthetic demonstration • not coursework benchmark", color=muted, fontsize=10)
    fig.text(0.10, 0.038, "Data seed 42  |  Algorithm initialization seed 42  |  MAlazmii / Clustering-Algorithms", color=muted, fontsize=9)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, facecolor=bg, metadata={"Date": None,
                "Title": "K-means synthetic demonstration",
                "Description": "Actual original k-means output on seeded synthetic data. Not a coursework benchmark. Source SHA256: " + source_hash})
    plt.close(fig)
    print(f"Saved {args.output}; cluster sizes: {[int(sum(labels == i)) for i in order]}")
    print(f"Source SHA256: {source_hash}")
    print("Verified finite centroids, nonempty clusters, nearest-centroid assignments, and centroid means.")


if __name__ == "__main__":
    main()
