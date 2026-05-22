# Papers Index

Last updated: 2026-05-22 14:44

## Paper Status

| # | PDF | Summary | Status | Tags |
|---:|---|---|---|---|
| 1 | [Flexible Isosurface Extraction for Gradient-Based Mesh Optimization.pdf](../papers/Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.pdf) | [summary/Flexible Isosurface Extraction for Gradient-Based Mesh Optimization.md](Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.md) | summarized | `isosurface extraction`, `differentiable mesh optimization`, `FlexiCubes`, `simulation-ready geometry`, `robotics simulation` |
| 2 | [Pixal3D_Pixel-Aligned 3D Generation from Images.pdf](../papers/Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.pdf) | 없음 | pending | 요약 후 작성 |
| 3 | [ReconViaGen_Towards Accurate Multi-view 3D Object Reconstruction via Generation.pdf](../papers/ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.pdf) | [summary/ReconViaGen_Towards Accurate Multi-view 3D Object Reconstruction via Generation.md](ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.md) | summarized | `multi-view reconstruction`, `diffusion prior`, `pose-free 3D reconstruction`, `robotics perception` |
| 4 | [SparseFlex_High-Resolution and Arbitrary-Topology 3D Shape Modeling.pdf](../papers/SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.pdf) | [summary/SparseFlex_High-Resolution and Arbitrary-Topology 3D Shape Modeling.md](SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.md) | summarized | `sparse isosurface`, `open-surface reconstruction`, `differentiable rendering`, `3D generation`, `robotics geometry` |

## Summaries

| # | PDF | 3-line summary |
|---:|---|---|
| 1 | [Flexible Isosurface Extraction for Gradient-Based Mesh Optimization.pdf](../papers/Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.pdf) | 1. FlexiCubes는 Dual Marching Cubes 기반 isosurface extraction에 최적화 가능한 interpolation, vertex positioning, quad splitting, grid deformation 자유도를 추가한다.<br>2. DMTet/MC보다 sharp feature alignment, normal consistency, edge fidelity, triangle quality가 좋아 nvdiffrec, GET3D, differentiable physics simulation에 plug-in으로 쓸 수 있다.<br>3. Self-intersection, discontinuity, memory overhead, tetrahedral/adaptive corner case는 남아 있어 robotics simulation이나 deployment 전 별도 mesh validation이 필요하다. |
| 2 | [Pixal3D_Pixel-Aligned 3D Generation from Images.pdf](../papers/Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.pdf) | 요약 전 |
| 3 | [ReconViaGen_Towards Accurate Multi-view 3D Object Reconstruction via Generation.pdf](../papers/ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.pdf) | 1. VGGT reconstruction prior와 TRELLIS generation prior를 결합해 pose-free multi-view object reconstruction을 수행한다.<br>2. GGC, PVC, RVC로 global shape, local detail, pixel-level alignment를 각각 개선한다.<br>3. Dora-Bench와 OmniObject3D에서 geometry accuracy와 completeness가 강하지만 hallucinated invisible geometry의 물리적 정답성은 추가 검증이 필요하다. |
| 4 | [SparseFlex_High-Resolution and Arbitrary-Topology 3D Shape Modeling.pdf](../papers/SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.pdf) | 1. SparseFlex는 FlexiCubes를 sparse voxel 구조로 확장해 open surface와 interior를 포함한 arbitrary-topology mesh를 rendering loss로 학습한다.<br>2. Frustum-aware sectional voxel training은 camera frustum 안의 voxel만 활성화해 $1024^3$급 고해상도 reconstruction의 memory 병목을 줄인다.<br>3. Toys4k, Dora Benchmark, Deepfashion3D에서 reconstruction/generation 성능은 강하지만 robotics deployment에는 mesh validity와 simulation 안정성 검증이 추가로 필요하다. |
