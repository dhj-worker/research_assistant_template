# TRELLIS: Structured 3D Latents for Scalable and Versatile 3D Generation

## Source

- Summary file: [`TRELLIS_Structured 3D Latents for Scalable and Versatile 3D Generation.md`](../TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md)
- PDF: `TRELLIS_Structured 3D Latents for Scalable and Versatile 3D Generation.pdf`

## Paper Card

- Core problem: 3D generation에서 output representation별 trade-off 때문에 geometry, appearance, rendering fidelity, downstream mesh usability를 동시에 만족하는 latent space를 만들기 어렵다.
- Core method: Sparse 3D grid 위 active voxel과 DINOv2 multiview local visual feature를 결합한 SLAT를 만들고, structure generation과 local latent generation을 분리한 two-stage rectified flow transformer로 text/image-conditioned 3D asset을 생성한다.
- Representation: Sparse voxel structure plus local latent feature인 SLAT; decoder 선택에 따라 3D Gaussian, Radiance Field, mesh로 변환된다.
- Input / output: Text prompt 또는 image condition을 입력으로 받아 SLAT를 생성하고, 최종적으로 Gaussian/Radiance Field/mesh 3D asset을 출력한다.
- Claimed improvement: 하나의 structured latent에서 여러 3D output format을 decoding해 기존 representation-specific latent의 한계를 줄이고, reconstruction과 text/image-to-3D generation에서 강한 품질을 보인다.
- Main baselines: LN3Diff, 3DTopia-XL, CLAY, Instant3D, LGM, CRM, Michelangelo, TripoSR, Shap-E, Point-E, MVDream, Direct3D, Rodin, Wonder3D 등.
- Limitations: Two-stage generation이 single-stage pipeline보다 비효율적일 수 있고, image-to-3D 결과에서 lighting/highlight가 baked-in될 수 있으며, PBR material prediction과 simulation-ready mesh validity는 직접 보장하지 않는다.
- Robotics relevance: Photorealistic synthetic data, perception simulation, scene asset generation, manipulation/planning 후보 mesh 생성에 유용하지만 metric scale, collision geometry, physical stability, inertia, contact behavior 검증이 필요하다.
- Related papers: [TRELLIS2](../TRELLIS2_Native%20and%20Compact%20Structured%20Latents%20for%203D%20Generation.md), Flexible Isosurface Extraction for Gradient-Based Mesh Optimization, SparseFlex, Pixal3D, ReconViaGen, SAM 3D.
- Open questions: SLAT에서 생성한 mesh를 robot simulation에 넣기 전에 어떤 automatic validation/repair pipeline이 필요한가? Multi-format decoding의 장점이 robotics benchmark에서 실제 task success로 이어지는가?

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
| uses-prior-from | [Flexible Isosurface Extraction](Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.md) | high | TRELLIS summary states that the mesh decoder uses FlexiCubes-based geometry generation. |
| provides-prior-to | [SparseFlex](SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.md) | high | SparseFlex summary describes a TRELLIS-like structure flow / structured latent flow setup and fine-tuning TRELLIS components. |
| provides-prior-to | [ReconViaGen](ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.md) | high | ReconViaGen summary states that it injects VGGT-derived conditions into TRELLIS SS Flow and SLAT Flow. |
| provides-prior-to | [TRELLIS2](TRELLIS2_Native%20and%20Compact%20Structured%20Latents%20for%203D%20Generation.md) | high | TRELLIS2 summary explicitly compares against TRELLIS and describes replacing multiview 2D feature-based SLAT with native O-Voxel structured latents. |
