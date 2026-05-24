# TRELLIS2: Native and Compact Structured Latents for 3D Generation

## Source

- Summary file: [`TRELLIS2_Native and Compact Structured Latents for 3D Generation.md`](../TRELLIS2_Native%20and%20Compact%20Structured%20Latents%20for%203D%20Generation.md)
- PDF: `TRELLIS2_Native and Compact Structured Latents for 3D Generation.pdf`

## Paper Card

- Core problem: 기존 3D representation은 open surface, non-manifold geometry, enclosed interior, detailed PBR appearance를 동시에 compact하게 표현하고 생성하기 어렵다.
- Core method: Mesh/PBR asset을 field-free sparse O-Voxel로 변환하고, Sparse Compression VAE로 compact structured latent를 만든 뒤, flow-matching DiT가 sparse structure, geometry latent, material latent를 순차 생성한다.
- Representation: O-Voxel 기반 native sparse 3D representation과 SC-VAE latent; shape feature는 Flexible Dual Grid, material feature는 base color, metallic, roughness, opacity를 포함한다.
- Input / output: 주로 image condition에서 high-resolution 3D asset을 생성하며, geometry와 PBR material이 align된 mesh/texture asset으로 변환될 수 있다.
- Claimed improvement: TRELLIS의 multiview 2D feature 기반 SLAT보다 native 3D/PBR data에서 직접 학습한 latent를 사용해 topology fidelity, material modeling, compression, high-resolution scaling을 개선한다.
- Main baselines: TRELLIS, Dora, Hunyuan3D 2.1, Step1X-3D, Direct3D-S2, Hi3DGen, Hunyuan3D-Paint, TEXGen.
- Limitations: Voxel보다 작은 parallel surface는 평균화될 수 있고, small hole이 생길 수 있으며, higher-level semantic/part/topological structure와 robot-relevant physical/contact parameters는 명시적으로 encode하지 않는다.
- Robotics relevance: Relighting 가능한 PBR material과 arbitrary-topology geometry는 synthetic perception data, domain randomization, embodied AI simulation asset에 중요하지만, scale, collision stability, mass/inertia, articulation, affordance, friction/contact parameter 검증은 별도 과제다.
- Related papers: [TRELLIS](../TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md), Flexible Isosurface Extraction for Gradient-Based Mesh Optimization, SparseFlex, Pixal3D, SAM 3D.
- Open questions: O-Voxel/SC-VAE latent가 physics-ready mesh generation까지 확장되려면 어떤 constraints나 post-processing이 필요한가? PBR material latent를 robot perception/simulation에서 필요한 sensor and contact material model로 확장할 수 있는가?

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
| improves | [TRELLIS](TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | Summary states that TRELLIS2 moves from TRELLIS's DINOv2 multiview feature-based SLAT to native O-Voxel latents and adds compact SC-VAE plus PBR material generation. |
