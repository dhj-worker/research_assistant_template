# Research Map

Last updated: 2026-05-24 10:39

## Purpose

이 문서는 개별 논문 summary 사이의 관계, 반복되는 문제의식, 연구 흐름, robotics 관점의 gap을 얇게 누적 기록한다. 자세한 논문별 분석은 `summary/research_cards/`의 카드 파일에 둔다.

## Paper Cards

| Paper | Summary | Card | Status | Main Themes |
|---|---|---|---|---|
| Flexible Isosurface Extraction for Gradient-Based Mesh Optimization | [summary](Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.md) | [card](research_cards/Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.md) | up-to-date | FlexiCubes, differentiable isosurface extraction, mesh optimization, physics simulation |
| Pixal3D: Pixel-Aligned 3D Generation from Images | [summary](Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.md) | [card](research_cards/Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.md) | up-to-date | pixel-aligned generation, back-projection conditioning, image-to-3D fidelity |
| SparseFlex: High-Resolution and Arbitrary-Topology 3D Shape Modeling | [summary](SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.md) | [card](research_cards/SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.md) | up-to-date | SparseFlex, high-resolution mesh, open surface, arbitrary topology |
| VGGT: Visual Geometry Grounded Transformer | [summary](VGGT_Visual%20Geometry%20Grounded%20Transformer.md) | [card](research_cards/VGGT_Visual%20Geometry%20Grounded%20Transformer.md) | up-to-date | feed-forward 3D reconstruction, camera/depth, point maps, tracking |
| VGGT-$\Omega$ | [summary](VGGT-Omega.md) | [card](research_cards/VGGT-Omega.md) | up-to-date | reconstruction scaling, register attention, dynamic reconstruction, spatial representation |
| ReconViaGen: Towards Accurate Multi-view 3D Object Reconstruction via Generation | [summary](ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.md) | [card](research_cards/ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.md) | up-to-date | generation-assisted reconstruction, VGGT prior, TRELLIS prior, pose-free multi-view |
| SAM 3D: 3Dfy Anything in Images | [summary](SAM%203D_3Dfy%20Anything%20in%20Images.md) | [card](research_cards/SAM%203D_3Dfy%20Anything%20in%20Images.md) | up-to-date | visually grounded 3D, shape/texture/layout, MITL data engine |
| TRELLIS: Structured 3D Latents for Scalable and Versatile 3D Generation | [summary](TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | [card](research_cards/TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | up-to-date | SLAT, structured 3D latent, rectified flow, multi-format decoding |
| TRELLIS2: Native and Compact Structured Latents for 3D Generation | [summary](TRELLIS2_Native%20and%20Compact%20Structured%20Latents%20for%203D%20Generation.md) | [card](research_cards/TRELLIS2_Native%20and%20Compact%20Structured%20Latents%20for%203D%20Generation.md) | up-to-date | O-Voxel, native 3D latent, PBR material, sparse compression VAE |

## Relations

| Source | Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|---|
| [Flexible Isosurface Extraction](research_cards/Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.md) | provides-prior-to | [TRELLIS](research_cards/TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | TRELLIS summary states that its mesh decoder is based on FlexiCubes. |
| [SparseFlex](research_cards/SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.md) | uses-prior-from | [Flexible Isosurface Extraction](research_cards/Flexible%20Isosurface%20Extraction%20for%20Gradient-Based%20Mesh%20Optimization.md) | high | SparseFlex summary states that it combines FlexiCubes accuracy with sparse voxel structure. |
| [SparseFlex](research_cards/SparseFlex_High-Resolution%20and%20Arbitrary-Topology%203D%20Shape%20Modeling.md) | uses-prior-from | [TRELLIS](research_cards/TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | SparseFlex summary describes a TRELLIS-like structure flow / structured latent flow setup and fine-tuning TRELLIS components. |
| [VGGT-$\Omega$](research_cards/VGGT-Omega.md) | improves | [VGGT](research_cards/VGGT_Visual%20Geometry%20Grounded%20Transformer.md) | high | VGGT-$\Omega$ summary explicitly frames the work as a scaling and architecture-efficiency successor to VGGT. |
| [ReconViaGen](research_cards/ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.md) | uses-prior-from | [VGGT](research_cards/VGGT_Visual%20Geometry%20Grounded%20Transformer.md) | high | ReconViaGen summary states that VGGT provides pose-free reconstruction features used as global/local conditions. |
| [ReconViaGen](research_cards/ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.md) | uses-prior-from | [TRELLIS](research_cards/TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | ReconViaGen summary states that it injects VGGT-derived conditions into TRELLIS SS Flow and SLAT Flow. |
| [TRELLIS2](research_cards/TRELLIS2_Native%20and%20Compact%20Structured%20Latents%20for%203D%20Generation.md) | improves | [TRELLIS](research_cards/TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | TRELLIS2 summary explicitly frames O-Voxel/SC-VAE as replacing TRELLIS's multiview 2D feature SLAT with native 3D/PBR structured latents. |
| [Pixal3D](research_cards/Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.md) | shares-baseline-with | [TRELLIS](research_cards/TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | Pixal3D summary reports single-view and multi-view comparisons against TRELLIS. |
| [Pixal3D](research_cards/Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.md) | shares-baseline-with | [VGGT](research_cards/VGGT_Visual%20Geometry%20Grounded%20Transformer.md) | high | Pixal3D summary reports multi-view comparison against VGGT. |
| [Pixal3D](research_cards/Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.md) | contrasts-with | [SAM 3D](research_cards/SAM%203D_3Dfy%20Anything%20in%20Images.md) | high | Pixal3D summary contrasts camera-aligned scene generation with SAM 3D's canonical object plus pose-estimation pipeline. |
| [SAM 3D](research_cards/SAM%203D_3Dfy%20Anything%20in%20Images.md) | uses-prior-from | [TRELLIS](research_cards/TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | SAM 3D summary notes that its latent backbone follows the TRELLIS / Xiang et al. 2025 structured latent line. |

## Themes

### Image-Grounded 3D Reconstruction

- VGGT unifies camera, depth, point map, and tracking feature prediction in a feed-forward multi-view transformer.
- VGGT-$\Omega$ scales this line with register attention, much larger supervised/unlabeled video data, and dynamic-scene benchmarks.
- ReconViaGen uses VGGT features to condition TRELLIS generation so multi-view reconstruction can combine observed-view consistency with generative completion.
- Pixal3D shifts image-to-3D generation from canonical object-space conditioning toward camera-aligned, back-projected pixel-to-3D correspondence.
- SAM 3D emphasizes recognition-driven reconstruction from natural images, jointly proposing object shape, texture, and camera-relative layout from image and mask.

### Structured 3D Latents

- TRELLIS introduces SLAT as a sparse voxel plus local feature latent that can decode to Gaussian, Radiance Field, or mesh.
- TRELLIS2 shifts the latent source from multiview 2D foundation features to native mesh/PBR O-Voxel data and compresses it with SC-VAE.

### Geometry Extraction / Mesh Optimization

- FlexiCubes treats isosurface extraction as an optimization-aware representation, adding local degrees of freedom for vertex positioning, quad splitting, and grid deformation.
- SparseFlex sparsifies the FlexiCubes-style representation to reach high-resolution open-surface and arbitrary-topology mesh reconstruction/generation.

### Robotics Deployment Gaps

- Both papers are useful for simulation asset candidates, but neither directly verifies metric scale, collision validity, physical stability, articulation, or robot affordances.
- FlexiCubes improves differentiable mesh quality but still requires validation for self-intersection, watertightness, tetrahedral quality, and simulation stability.
- Feed-forward reconstruction models such as VGGT/VGGT-$\Omega$ are strong initializers, but robotics use still needs metric scale, calibration, temporal consistency, and domain-shift checks.
- ReconViaGen's generative completion is attractive for occluded objects, but hallucinated invisible geometry should be treated as a proposal unless uncertainty or physical validation is added.
- Pixal3D and SAM 3D make object/scene asset proposals more visually grounded, but robot use still needs uncertainty handling, scale calibration, contact validation, and sensor-noise stress tests.

## Research Questions

- How should generated SLAT/O-Voxel assets be validated or repaired before use as robot simulation assets?
- Can native PBR material latents be extended toward contact-relevant material parameters such as friction, compliance, and transparency behavior under robot sensors?
- Can differentiable isosurface extraction regularizers be coupled with robot simulation losses to produce meshes that are visually accurate and physically stable?
- When should robot perception pipelines prefer generative completion over conservative observed-surface reconstruction?
