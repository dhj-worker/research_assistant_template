# SAM 3D: 3Dfy Anything in Images

## Source

- Summary file: [`SAM 3D_3Dfy Anything in Images.md`](../SAM%203D_3Dfy%20Anything%20in%20Images.md)
- PDF: `SAM 3D_3Dfy Anything in Images.pdf`

## Paper Card

- Core problem: Single-image 3D reconstruction은 natural image의 clutter, occlusion, scale, pose, context cue를 충분히 활용하지 못해 real-world object shape, texture, camera-relative layout을 안정적으로 복원하기 어렵다.
- Core method: Image와 object mask를 조건으로 coarse shape/layout을 생성하는 Geometry model과 geometry detail/texture를 보강하는 Texture & Refinement model을 결합하고, Iso-3DO pretraining, RP-3DO mid-training, MITL/artist post-training, DPO alignment로 real-world visual grounding을 강화한다.
- Representation: Coarse voxel shape latent, explicit camera-relative layout parameters, SLAT 계열 sparse latent refinement, mesh 또는 Gaussian splat decoder.
- Input / output: Single natural image와 target object mask, 선택적 pointmap을 입력으로 받아 object shape, texture, rotation, translation, scale을 출력한다.
- Claimed improvement: Synthetic-only image-to-3D보다 natural image의 occlusion과 clutter에 강하고, SA-3DAO와 ADT에서 shape/layout metric 및 human preference를 개선한다.
- Main baselines: TRELLIS, Hunyuan3D, Direct3D-S2, TripoSG, Hi3DGen, FoundationPose, MegaPose, HY3D.
- Limitations: Output resolution이 제한되고, object-wise independent layout이라 contact, support, interpenetration, scene-level physical consistency를 보장하지 않으며, texture prediction이 pose ambiguity에 취약할 수 있다.
- Robotics relevance: Open-world object shape/layout proposal, scene understanding, simulation asset bootstrapping, pose initialization에 유용하지만 final state estimator로 쓰려면 RGB-D tracking, physics-aware optimization, collision checking, grasp feasibility 검증과 결합해야 한다.
- Related papers: [TRELLIS](../TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md), [Pixal3D](../Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.md), Hunyuan3D, Direct3D-S2, TripoSG, Hi3DGen.
- Open questions: Recognition-driven plausible 3D completion을 robot planning에서 uncertainty-aware proposal로 다루는 방법은 무엇인가? Object-wise generated layouts에 support/contact/scene constraints를 어떻게 후처리 또는 joint modeling으로 넣을 수 있는가?

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
| uses-prior-from | [TRELLIS](TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | Summary notes that SAM 3D's shape and texture/refinement latent design follows the TRELLIS / Xiang et al. 2025 structured latent line. |
| contrasts-with | [Pixal3D](Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.md) | high | Pixal3D summary contrasts camera-aligned generation with SAM 3D's canonical object plus pose-estimation scene pipeline. |
