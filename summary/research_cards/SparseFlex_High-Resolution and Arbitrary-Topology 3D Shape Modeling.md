# SparseFlex: High-Resolution and Arbitrary-Topology 3D Shape Modeling

## Source

- Summary file: [`SparseFlex_High-Resolution and Arbitrary-Topology 3D Shape Modeling.md`](../SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.md)
- PDF: `SparseFlex_High-Resolution and Arbitrary-Topology 3D Shape Modeling.pdf`

## Paper Card

- Core problem: High-fidelity 3D mesh reconstruction/generation에서 watertight conversion과 dense grid memory 때문에 open surface, interior, arbitrary topology를 고해상도로 직접 다루기 어렵다.
- Core method: FlexiCubes-style differentiable isosurface extraction을 surface-adjacent sparse voxel set에만 적용하고, frustum-aware sectional voxel training으로 rendering supervision의 memory 병목을 줄인다.
- Representation: Sparse voxel center set $V$와 corner SDF/deformation $F_c=\{s_j,\delta_j\}$, voxel interpolation weights $F_v=\{\alpha_i,\beta_i\}$로 구성된 SparseFlex representation.
- Input / output: Point cloud 또는 image condition에서 sparse voxel structure와 SparseFlex VAE latent를 만들고, 최종적으로 open-surface와 interior를 포함할 수 있는 high-resolution mesh를 출력한다.
- Claimed improvement: FlexiCubes의 mesh fidelity를 sparse 구조로 확장해 $1024^3$급 reconstruction을 가능하게 하고, Toys4k/Dora/Deepfashion3D에서 CD/F-score 및 generation FID/KID를 개선한다.
- Main baselines: Craftsman, Dora, TRELLIS, XCube, Surf-D, 3PSDF, InstantMesh, Direct3D.
- Limitations: Open boundary artifact, high-resolution compute cost, interior control 부족, physical validity/manifoldness/self-intersection/collision stability 검증 부족이 남는다.
- Robotics relevance: 의류, 케이블, 식물, 얇은 플라스틱처럼 watertight conversion이 부적절한 object의 reconstruction prior로 유용하며, collision/FEM/contact simulation으로 넘기려면 mesh validation과 repair가 필요하다.
- Related papers: [Flexible Isosurface Extraction](../Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.md), [TRELLIS](../TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md), TRELLIS2, 3PSDF, Surf-D.
- Open questions: SparseFlex mesh를 robot planning용 collision mesh로 바꾸기 위한 post-processing/validation 기준은 무엇인가? Interior reconstruction을 실제 robot sensor trajectory나 active perception과 결합할 수 있는가?

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
| uses-prior-from | [Flexible Isosurface Extraction](Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.md) | high | Summary states that SparseFlex combines FlexiCubes accuracy with sparse voxel structure. |
| uses-prior-from | [TRELLIS](TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | Summary describes a TRELLIS-like structure flow / structured latent flow setup and fine-tuning TRELLIS components. |
