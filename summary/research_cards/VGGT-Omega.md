# VGGT-$\Omega$

## Source

- Summary file: [`VGGT-Omega.md`](../VGGT-Omega.md)
- PDF: `VGGT-Omega.pdf`

## Paper Card

- Core problem: VGGT-style feed-forward reconstruction은 강하지만, many-frame/global attention memory, multi-head dense decoding cost, data scale, dynamic scene generalization이 scaling bottleneck으로 남는다.
- Core method: Register attention, single dense depth head, training-only point/matching losses, larger supervised annotation pipeline, teacher-student self-supervised learning으로 feed-forward reconstruction을 static/dynamic scene까지 scale한다.
- Representation: DINOv3-initialized visual tokens, per-frame camera token, scene register tokens, camera $g_i=(q_i,t_i,f_i)$, depth map $D_i$, training-only point/matching supervision.
- Input / output: Multi-view image sequence를 입력으로 받아 각 frame의 camera parameter와 depth map을 feed-forward로 출력하고, learned scene registers를 spatial representation으로 활용한다.
- Claimed improvement: VGGT 대비 memory-efficient architecture와 훨씬 큰 supervised/unlabeled video data로 static/dynamic camera pose와 depth benchmark를 개선하고, frozen register가 VLA와 language alignment에도 유용함을 보인다.
- Main baselines: VGGT, DUSt3R, MASt3R, MegaSaM, DA3, PI3, COLMAP/SfM/MVS, OpenVLA-OFT baseline.
- Limitations: Strong motion blur, 급격한 FOV 변화, distorted camera, noisy pseudo-label, masked/blurred training regions에서 failure가 있으며, 10B model은 onboard robotics deployment에 부담이 크다.
- Robotics relevance: 강한 feed-forward geometry initializer이자 spatial representation backbone으로, robot pose/depth initialization, VLA scene token, active reconstruction prior에 유용하지만 scale calibration, sensor fusion, rolling shutter, wide-FOV, closed-loop robustness 검증이 필요하다.
- Related papers: [VGGT](../VGGT_Visual%20Geometry%20Grounded%20Transformer.md), ReconViaGen, DUSt3R, MASt3R, MegaSaM, OpenVLA.
- Open questions: Reconstruction-pretrained registers가 실제 closed-loop robot manipulation에서 어떤 spatial error mode를 줄이는가? Register attention의 efficiency/accuracy trade-off를 onboard GPU에 맞게 조절할 수 있는가?

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
| improves | [VGGT](VGGT_Visual%20Geometry%20Grounded%20Transformer.md) | high | Summary explicitly presents VGGT-$\Omega$ as a scaling, efficiency, and dynamic-scene successor to VGGT. |
