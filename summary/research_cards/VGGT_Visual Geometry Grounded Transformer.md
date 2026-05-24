# VGGT: Visual Geometry Grounded Transformer

## Source

- Summary file: [`VGGT_Visual Geometry Grounded Transformer.md`](../VGGT_Visual%20Geometry%20Grounded%20Transformer.md)
- PDF: `VGGT_Visual Geometry Grounded Transformer.pdf`

## Paper Card

- Core problem: Classical visual geometry는 SfM/MVS/tracking 등 task별 optimization-heavy pipeline으로 나뉘어 있어, fast pose-free multi-view geometry estimation이 어렵다.
- Core method: DINOv2 tokenization과 alternating frame-wise/global self-attention transformer를 사용해 camera, depth, point map, tracking feature를 하나의 feed-forward network에서 multi-task로 예측한다.
- Representation: Multi-view visual tokens, camera tokens, dense DPT features, camera parameter $g=[q,t,f]$, depth map, first-camera-frame point map, tracking feature grid.
- Input / output: 하나, 몇 개, 또는 수백 개 RGB view를 입력으로 받아 각 view의 camera parameter, depth map, world-coordinate point map, point tracking feature를 출력한다.
- Claimed improvement: Pairwise prediction과 global alignment 또는 BA에 강하게 의존하던 기존 neural geometry pipeline보다 빠르고, camera pose, MVS, point map, matching benchmark에서 강한 성능을 보인다.
- Main baselines: COLMAP/SfM/MVS, DUSt3R, MASt3R, VGGSfM, Fast3R, MVSNet/GeoMVSNet, SuperGlue, LoFTR, DKM, Roma, CoTracker.
- Limitations: Fisheye/panorama 미지원, extreme rotation과 large non-rigid motion failure, 수백 frame global attention memory cost, absolute metric scale/calibration ambiguity가 남는다.
- Robotics relevance: SLAM/BA/3DGS/mesh reconstruction 초기값, robot-collected image burst의 pose/depth prior, visual servoing과 manipulation tracking feature로 유용하지만 metric scale, calibration, temporal consistency, wide-FOV/domain shift 검증이 필요하다.
- Related papers: [VGGT-$\Omega$](../VGGT-Omega.md), [ReconViaGen](../ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.md), DUSt3R, MASt3R, VGGSfM.
- Open questions: VGGT를 robot SLAM의 feed-forward initializer로 쓸 때 BA/loop closure와 어떤 interface가 가장 안정적인가? Learned correspondence feature가 manipulation keypoint tracking에서 얼마나 robust한가?

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
| provides-prior-to | [VGGT-$\Omega$](VGGT-Omega.md) | high | VGGT-$\Omega$ summary frames itself as scaling and simplifying the VGGT feed-forward reconstruction line. |
| provides-prior-to | [ReconViaGen](ReconViaGen_Towards%20Accurate%20Multi-view%203D%20Object%20Reconstruction%20via%20Generation.md) | high | ReconViaGen summary states that VGGT features provide pose-free reconstruction priors for global/local generation conditions. |
