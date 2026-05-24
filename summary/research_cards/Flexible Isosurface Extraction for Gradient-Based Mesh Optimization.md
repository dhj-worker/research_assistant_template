# Flexible Isosurface Extraction for Gradient-Based Mesh Optimization

## Source

- Summary file: [`Flexible Isosurface Extraction for Gradient-Based Mesh Optimization.md`](../Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.md)
- PDF: `Flexible Isosurface Extraction for Gradient-Based Mesh Optimization.pdf`

## Paper Card

- Core problem: Gradient-based mesh optimization에서 classic isosurface extraction은 fixed field extraction용으로 설계되어 feature-preserving geometry, stable gradients, high-quality tessellation을 동시에 만족하기 어렵다.
- Core method: Dual Marching Cubes 기반 extraction에 flexible vertex positioning, flexible quad splitting, flexible grid deformation을 추가하고, 이 parameters를 scalar field와 함께 automatic differentiation으로 최적화한다.
- Representation: Scalar field의 $0$-isosurface를 DMC-style dual mesh로 추출하되, trainable interpolation/vertex/splitting/deformation parameters를 가진 FlexiCubes representation.
- Input / output: Grid 위 scalar field와 추가 FlexiCubes parameters를 입력으로 받아 surface mesh를 추출하며, 선택적으로 tetrahedral mesh와 adaptive-resolution mesh도 생성한다.
- Claimed improvement: MC/DMTet보다 sharp feature alignment, normal consistency, edge fidelity, triangle quality가 좋고, nvdiffrec, GET3D, differentiable physics simulation 같은 downstream pipeline에 plug-in으로 적용 가능하다.
- Main baselines: Marching Cubes, Marching Tetrahedra, Dual Contouring, Dual Marching Cubes, Neural Dual Contouring, DMTet, template mesh deformation.
- Limitations: Self-intersection-free와 global continuity/formal differentiability를 보장하지 않고, MC/DMTet보다 runtime과 memory가 크며, tetrahedral/adaptive extension에는 tiny-volume element나 non-manifold corner case가 남는다.
- Robotics relevance: Perception-to-simulation, differentiable rendering, deformable object simulation, inverse physics, manipulation planning용 mesh 후보 생성에 중요하지만, watertightness, collision validity, tetrahedral conditioning, contact stability 검증이 필요하다.
- Related papers: [TRELLIS](../TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md), SparseFlex, TRELLIS2, GET3D, nvdiffrec, DMTet.
- Open questions: FlexiCubes의 differentiable extraction parameters를 robot simulation loss와 함께 학습하면 visually accurate하면서 physically stable한 mesh를 얻을 수 있는가? Self-intersection과 tetrahedral quality를 보장하는 stronger regularizer를 어떻게 넣을 수 있는가?

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
| provides-prior-to | [TRELLIS](TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | TRELLIS summary states that its mesh decoder is based on FlexiCubes. |
| provides-prior-to | [SparseFlex](SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.md) | high | SparseFlex summary states that it combines FlexiCubes accuracy with sparse voxel structure. |
