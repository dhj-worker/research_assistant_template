# Pixal3D: Pixel-Aligned 3D Generation from Images

## Source

- Summary file: [`Pixal3D_Pixel-Aligned 3D Generation from Images.md`](../Pixal3D_Pixel-Aligned%203D%20Generation%20from%20Images.md)
- PDF: `Pixal3D_Pixel-Aligned 3D Generation from Images.pdf`

## Paper Card

- Core problem: 기존 image-to-3D generator가 canonical space에서 이미지를 attention condition으로만 주입하면서 입력 이미지의 pixel-level detail과 3D latent 사이 correspondence가 모호해지는 fidelity 병목.
- Core method: 입력 camera frame에 정렬된 pixel-aligned 3D generation을 정의하고, DINOv2 multi-scale image feature를 camera projection으로 3D feature volume에 back-project해 diffusion noise volume에 직접 결합한다.
- Representation: Pixel-aligned sparse voxel / SDF latent diffusion backbone과 back-projected 3D feature volume condition.
- Input / output: Single-view 또는 known-pose multi-view image를 입력으로 받아 입력 view와 정렬된 object mesh 및 object-separated scene asset을 생성한다.
- Claimed improvement: Canonical-pose generation 대비 visible surface detail, silhouette, part arrangement fidelity를 reconstruction 수준에 가깝게 끌어올리고 multi-view feature aggregation으로 geometry accuracy를 개선한다.
- Main baselines: TRELLIS, TripoSG, Hunyuan3D-2.1, Direct3D-S2, VGGT, SAM 3D.
- Limitations: Pixel-level noise와 segmentation boundary error가 3D artifact로 증폭될 수 있고, multi-view에서는 camera pose 정확도를 가정하며, scene pipeline은 2D inpainting과 scale/depth alignment heuristic에 의존한다.
- Robotics relevance: Observation-aligned mesh asset은 manipulation, collision checking, active perception, scene reconstruction에 유용하지만 metric scale, physical validity, watertightness, contact stability, real sensor noise robustness 검증이 추가로 필요하다.
- Related papers: [TRELLIS](../TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md), [VGGT](../VGGT_Visual%20Geometry%20Grounded%20Transformer.md), [SAM 3D](../SAM%203D_3Dfy%20Anything%20in%20Images.md), Direct3D-S2, TripoSG, Hunyuan3D.
- Open questions: Pixel-aligned generation을 robot RGB-D / multi-view capture에서 pose uncertainty와 segmentation uncertainty까지 포함해 fusion할 수 있는가? Generated visible-surface fidelity가 grasp/contact planning 성공률로 이어지는지 어떤 benchmark로 검증할 것인가?

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
| shares-baseline-with | [TRELLIS](TRELLIS_Structured%203D%20Latents%20for%20Scalable%20and%20Versatile%203D%20Generation.md) | high | Summary reports single-view and multi-view comparisons against TRELLIS. |
| shares-baseline-with | [VGGT](VGGT_Visual%20Geometry%20Grounded%20Transformer.md) | high | Summary reports multi-view comparison against VGGT. |
| contrasts-with | [SAM 3D](SAM%203D_3Dfy%20Anything%20in%20Images.md) | high | Summary contrasts Pixal3D's camera-aligned scene generation with SAM 3D's canonical object plus pose-estimation pipeline. |
