# ReconViaGen: Towards Accurate Multi-view 3D Object Reconstruction via Generation

## Source

- Summary file: [`ReconViaGen_Towards Accurate Multi-view 3D Object Reconstruction via Generation.md`](../ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.md)
- PDF: `ReconViaGen_Towards Accurate Multi-view 3D Object Reconstruction via Generation.pdf`

## Paper Card

- Core problem: Sparse/occluded multi-view object reconstruction은 observed geometry에는 맞지만 incomplete해지기 쉽고, diffusion 3D generation은 invisible part를 완성하지만 input-view consistency와 local detail alignment가 약하다.
- Core method: VGGT reconstruction feature를 Global Geometry Condition과 Local Per-View Condition으로 바꿔 TRELLIS SS Flow/SLAT Flow에 주입하고, inference 중 Rendering-aware Velocity Compensation으로 denoising trajectory를 input render consistency 쪽으로 보정한다.
- Representation: VGGT-derived 3D-aware condition tokens, TRELLIS sparse structure and SLAT latent, rendering-aware velocity correction을 결합한 generation-assisted reconstruction pipeline.
- Input / output: Calibration 없는 arbitrary multi-view object images를 입력으로 받아 input view와 정합적인 complete textured 3D asset/mesh를 출력한다.
- Claimed improvement: VGGT류 reconstruction의 incompleteness와 TRELLIS류 diffusion generation의 stochastic inconsistency를 동시에 줄여 Dora-Bench와 OmniObject3D에서 rendering/geometry metric을 개선한다.
- Main baselines: TRELLIS-S, TRELLIS-M, Hunyuan3D-2.0-mv, InstantMesh, LGM, LucidFusion, VGGT, Hunyuan3D-2.5, Meshy-5.
- Limitations: Diffusion completion은 invisible geometry의 실제 정답성을 보장하지 않고, RVC는 pose refinement 품질에 의존하며, physical validity, metric scale, contact geometry, reflective/transparent/articulated/deformable robustness는 충분히 검증되지 않았다.
- Robotics relevance: Robot wrist/handheld multi-view capture에서 occluded object completion proposal로 유용하지만, grasp/planning ground truth로 쓰려면 uncertainty, collision validation, metric scale alignment, physical plausibility checks가 필요하다.
- Related papers: [VGGT](../VGGT_Visual%20Geometry%20Grounded%20Transformer.md), [TRELLIS](../TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md), DUSt3R, Hunyuan3D, InstantMesh, LucidFusion.
- Open questions: Generative completion의 hallucinated backside를 robot planning에서 어떻게 uncertainty-aware proposal로 다룰 수 있는가? RVC-style rendering guidance를 depth/contact/physics loss까지 확장할 수 있는가?

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
| uses-prior-from | [VGGT](VGGT_Visual%20Geometry%20Grounded%20Transformer.md) | high | Summary states that VGGT provides pose-free reconstruction features used for global and local conditions. |
| uses-prior-from | [TRELLIS](TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | Summary states that ReconViaGen injects VGGT-derived conditions into TRELLIS SS Flow and SLAT Flow. |
