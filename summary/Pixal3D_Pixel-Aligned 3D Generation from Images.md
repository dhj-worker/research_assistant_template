# Pixal3D: Pixel-Aligned 3D Generation from Images

## 메타데이터

- PDF 파일: `Pixal3D_Pixel-Aligned 3D Generation from Images.pdf`
- 논문 제목: Pixal3D: Pixel-Aligned 3D Generation from Images
- 저자: Dong-Yang Li, Wang Zhao, Yuxin Chen, Wenbo Hu, Meng-Hao Guo, Fang-Lue Zhang, Ying Shan, Shi-Min Hu
- venue/arXiv: SIGGRAPH Conference Papers '26; arXiv:2605.10922v1 [cs.CV]
- 연도: 2026
- DOI/URL: https://doi.org/10.1145/3799902.3811175; https://ldyang694.github.io/projects/pixal3d/
- 작업 일시: 2026-05-22 16:31

## Abstract

Recent advances in 3D generative models have rapidly improved image-to-3D synthesis quality, enabling higher-resolution geometry and more realistic appearance.

**최근 3D generative model의 발전은 image-to-3D 합성 품질을 빠르게 끌어올려, 더 높은 해상도의 geometry와 더 사실적인 appearance를 가능하게 했다.**

Yet fidelity, which measures pixel-level faithfulness of the generated 3D asset to the input image, still remains a central bottleneck.

**그러나 생성된 3D asset이 입력 이미지에 pixel-level로 얼마나 충실한지를 측정하는 fidelity는 여전히 핵심 병목으로 남아 있다.**

We argue this stems from an implicit 2D-3D correspondence issue: most 3D-native generators synthesize shape in canonical space and inject image cues via attention, leaving pixel-to-3D associations ambiguous.

**저자들은 이 문제가 implicit 2D-3D correspondence에서 비롯된다고 주장한다. 대부분의 3D-native generator는 canonical space에서 shape를 합성하고 attention을 통해 image cue를 주입하기 때문에, pixel과 3D 위치 사이의 대응이 모호하게 남는다.**

To tackle this issue, we draw inspiration from 3D reconstruction and propose Pixal3D, a pixel-aligned 3D generation paradigm for high-fidelity 3D asset creation from images.

**이 문제를 해결하기 위해 저자들은 3D reconstruction에서 영감을 얻어, 이미지로부터 high-fidelity 3D asset을 만들기 위한 pixel-aligned 3D generation paradigm인 Pixal3D를 제안한다.**

Instead of generating in a canonical pose, Pixal3D directly generates 3D in a pixel-aligned way, consistent with the input view.

**Pixal3D는 canonical pose에서 생성하는 대신, 입력 view와 일치하는 pixel-aligned 방식으로 3D를 직접 생성한다.**

To enable this, we introduce a pixel back-projection conditioning scheme that explicitly lifts multi-scale image features into a 3D feature volume, establishing direct pixel-to-3D correspondence without ambiguity.

**이를 위해 저자들은 multi-scale image feature를 3D feature volume으로 명시적으로 lift하는 pixel back-projection conditioning scheme을 도입하여, 모호성 없는 직접적인 pixel-to-3D correspondence를 만든다.**

We show that Pixal3D is not only scalable and capable of producing high-quality 3D assets, but also substantially improves fidelity, approaching the fidelity level of reconstruction.

**Pixal3D는 scalable하고 고품질 3D asset을 생성할 수 있을 뿐 아니라, fidelity를 크게 개선해 reconstruction 수준에 가까운 fidelity에 도달함을 보인다.**

Furthermore, Pixal3D naturally extends to multi-view generation by aggregating back-projected feature volumes across views.

**또한 Pixal3D는 여러 view에서 back-projection된 feature volume을 aggregation함으로써 multi-view generation으로 자연스럽게 확장된다.**

Finally, we show pixel-aligned generation benefits scene synthesis, and present a modular pipeline that produces high-fidelity, object-separated 3D scenes from images.

**마지막으로 저자들은 pixel-aligned generation이 scene synthesis에도 이점을 준다는 점을 보이고, 이미지로부터 high-fidelity이면서 object-separated인 3D scene을 생성하는 modular pipeline을 제시한다.**

Pixal3D for the first time demonstrates 3D-native pixel-aligned generation at scale, and provides a new inspiring way towards high-fidelity 3D generation of object or scene from single or multi-view images.

**Pixal3D는 3D-native pixel-aligned generation이 scale 있게 가능함을 처음으로 보이며, single-view 또는 multi-view 이미지로부터 object나 scene을 high-fidelity 3D로 생성하는 새로운 방향을 제시한다.**

Project page: https://ldyang694.github.io/projects/pixal3d/

**프로젝트 페이지: https://ldyang694.github.io/projects/pixal3d/**

## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 다시 확인한다.

1. Introduction
2. Related Works
   1. 3D Generation
   2. 3D Reconstruction
   3. 3D Generative Reconstruction
3. Method
   1. Preliminary
   2. Pixel-aligned 3D Generation
      1. Canonical vs. Pixel-Aligned Generation
      2. Back-projection Conditioned 3D Latent Diffusion
      3. Multi-view Extension
   3. Scene Generation Pipeline
   4. Implementation Details
4. Experiments
   1. Single-view 3D Generation
   2. Multi-view 3D Generation
   3. 3D Scene Generation
   4. Ablation Studies
   5. Limitations and Future Works
5. Conclusion

Section/subsection heading 누락 여부는 `full.txt`와 `raw_full.txt`의 heading 검색으로 다시 확인했다.

## 요약

### 1. 전체 구조

Pixal3D는 image-to-3D generation의 병목을 "quality"보다 더 좁은 의미의 fidelity 문제로 정의한다. 여기서 fidelity는 생성 3D asset이 입력 이미지의 pixel-level detail, silhouette, part arrangement, fine structure를 얼마나 충실히 보존하는지를 뜻한다. 저자들의 핵심 진단은 기존 3D-native generator가 canonical object space에서 shape를 만들고 image feature를 cross-attention으로 주입하기 때문에, 어떤 image pixel이 어떤 3D latent/voxel에 영향을 주어야 하는지가 학습된 attention에 맡겨진다는 점이다.

논문은 이를 reconstruction의 관점으로 뒤집는다. Reconstruction 계열은 depth, normal, point map, MVS 등에서 pixel과 3D ray/point 사이의 correspondence를 명시적으로 다루기 때문에 visible surface fidelity가 높다. Pixal3D는 이 명시적 correspondence를 3D generative model에 넣어, visible region은 reconstruction처럼 강하게 constrain하고 invisible region은 generative prior로 plausible하게 completion하는 "3D generative reconstruction" paradigm으로 정식화한다.

방법론은 Direct3D-S2 계열의 sparse voxel latent diffusion backbone을 유지하되, 두 가지를 바꾼다. 첫째, canonical pose latent 대신 입력 camera view에 정렬된 pixel-aligned 3D latent를 학습한다. 둘째, image condition을 cross-attention 중심으로 넣는 대신, DINOv2 multi-scale feature를 3D volume으로 back-project하여 diffusion noise volume에 spatially aligned condition으로 더한다. 이 구조는 single-view, multi-view, object-separated scene generation으로 확장된다.

### 2. Section 간 연결

Introduction은 fidelity 병목을 정의하고, 그 원인을 implicit 2D-3D correspondence로 해석한다. Related Works는 3D generation, 3D reconstruction, 3D generative reconstruction을 분리해 비교하면서, Pixal3D가 reconstruction의 explicit correspondence를 generation의 complete asset prior와 결합하는 위치에 있음을 만든다.

Method는 먼저 Direct3D-S2의 dense/sparse latent diffusion pipeline을 base로 설명한 뒤, canonical generation과 pixel-aligned generation의 차이를 도식화한다. 이후 back-projection conditioner가 image feature를 voxel-aligned 3D feature volume으로 바꾸는 방식, multi-scale feature upsampling이 fine detail fidelity를 개선하는 이유, multi-view에서는 view별 feature volume을 평균 aggregation하는 방식을 설명한다. Scene generation section은 object crop을 각각 Pixal3D로 생성한 뒤 depth/point-map cue로 global alignment를 푸는 modular pipeline을 추가한다.

Experiments는 세 단계로 이어진다. Single-view에서는 Toys4K normal rendering metric과 in-the-wild user study로 fidelity를 검증한다. Multi-view에서는 VGGT와 TRELLIS against CD/EMD/F-Score를 비교한다. Scene generation은 SAM3D와 qualitative comparison을 통해 canonical pose/object pose estimation을 피하는 장점을 보인다. Ablation은 back-projection conditioning과 feature upsampling의 필요성을 따로 확인한다.

### 3. 핵심 주장과 근거

- 핵심 주장 1: image-to-3D fidelity 병목은 canonical-space generation과 cross-attention conditioning이 만드는 ambiguous 2D-3D correspondence에서 온다.
  - 근거: 기존 TRELLIS, TripoSG, Hunyuan3D-2.1, Direct3D-S2는 시각적으로 keyboard layout, face detail, flower petal count 같은 fine detail에서 입력 이미지와 misalignment를 보인다.
  - 해석: attention이 semantic-level guidance에는 강하지만, pixel-to-voxel assignment를 geometric하게 보장하지 못한다는 주장이다.

- 핵심 주장 2: pixel-aligned camera-space generation과 back-projected feature volume은 reconstruction-level fidelity에 접근한다.
  - 근거: Toys4K single-view normal comparison에서 Pixal3D는 IoU 93.57, PSNR 24.21, SSIM 0.897, LPIPS 0.108, mean angular error 16.63으로 모든 baseline보다 좋다.
  - 특히 Direct3D-S2가 같은 backbone 계열인데 IoU 74.23, PSNR 19.49, LPIPS 0.268에 머무르는 점은 conditioning 방식 차이의 evidence로 읽힌다.

- 핵심 주장 3: 같은 formulation이 multi-view에도 자연스럽게 확장된다.
  - 근거: Toys4K multi-view에서 Pixal3D는 view 2/4/6 모두 CD와 EMD가 낮고 F-Score가 높다. 예를 들어 view 6에서 VGGT는 CD 2791.10, F-Score 9.67, TRELLIS는 CD 18.13, F-Score 46.02인 반면 Pixal3D는 CD 4.16, F-Score 69.04를 보고한다.
  - 해석: view가 늘수록 generative ambiguity가 줄고 reconstruction cue가 강해진다는 논문 주장과 맞는다.

- 핵심 주장 4: scene generation에서는 object pose estimation을 피할 수 있어 alignment가 단순해진다.
  - 근거: SAM3D는 canonical geometry와 per-object 7-DoF pose를 추정해야 하지만, Pixal3D는 object가 input camera frame에 이미 정렬되어 있어 scale/depth를 MoGe point map과 least-squares constraint로 맞추는 방향을 택한다.

### 4. Robotics 관점의 novelty와 relevance

Robotics 관점에서 중요한 novelty는 "생성형 3D asset"을 단순히 plausibility 중심으로 만들지 않고, observed image frame과 직접 align된 geometry로 만드는 점이다. 로봇이 RGB 이미지 또는 multi-view observation에서 object mesh를 만들 때, canonical pose의 예쁜 mesh보다 camera observation과 silhouette/detail이 잘 맞는 mesh가 manipulation, collision checking, sim-to-real asset construction에 더 직접적으로 쓸 수 있다.

특히 pixel-aligned representation은 다음 작업에 relevance가 크다.

- Object-centric manipulation: visible surface가 input image와 잘 맞으면 grasp point, contact region, affordance localization을 mesh로 옮길 때 correspondence error가 줄어든다.
- Scene reconstruction for planning: object-separated scene pipeline은 SAM3D류 segmentation 기반 scene asset construction과 맞닿아 있어, tabletop scene이나 cluttered object scene을 simulation-ready primitive로 변환하는 데 유용할 수 있다.
- Multi-view active perception: multi-view extension은 camera pose가 알려진 경우 view 수가 늘어날수록 ambiguity가 줄어드는 구조라, 로봇이 next-best-view로 관측을 추가하는 setting과 잘 맞는다.
- Interactive editing: 논문이 future work로 언급하듯 pixel manipulation이 3D editing으로 이어질 수 있다면, 2D annotation 기반 robot scene correction이나 human-in-the-loop asset editing으로 확장 가능하다.

다만 robotics deployment에는 아직 빠진 부분이 있다. 본 논문은 geometry fidelity 중심이고, texture/material/PBR, physical stability, watertightness after generation, collision safety, object scale metric calibration, articulated/dynamic object handling은 직접 검증하지 않는다. 따라서 generated mesh를 motion planning이나 contact simulation에 바로 넣기보다는, mesh repair, scale calibration, physical validation을 추가해야 한다.

### 5. 기존 방법과 비교

| 구분 | 기존 방법 | Pixal3D | 의미 |
|---|---|---|---|
| Condition injection | Image feature를 cross-attention으로 3D latent에 주입 | DINOv2 feature를 camera frustum 기준으로 3D feature volume에 back-project하고 noise volume에 spatially add | pixel-to-3D 대응을 학습된 attention보다 geometric prior로 강제 |
| Coordinate frame | Canonical object pose에서 generation | Input camera view와 일치하는 pixel-aligned pose에서 generation | visible surface fidelity와 image alignment가 개선됨 |
| Single-view baseline | TRELLIS, TripoSG, Hunyuan3D-2.1, Direct3D-S2 | Toys4K normal metric에서 IoU 93.57, LPIPS 0.108 | 같은 image-to-3D setting에서 fidelity 중심 성능 우위 |
| Multi-view baseline | VGGT는 reconstruction point cloud가 noisy/floaters, TRELLIS는 smooth하지만 cross-view fidelity 한계 | view별 back-projected feature volume을 average aggregation | camera pose가 알려진 multi-view에서 simple하고 효과적인 fusion |
| Scene generation | SAM3D는 canonical object와 per-object 7-DoF pose 추정 필요 | object crop을 camera-aligned로 생성하고 scale/depth만 정렬 | multi-object alignment의 ill-posed pose estimation 부담 감소 |
| Fine detail | Coarse semantic feature 또는 high-res attention cost 문제 | NAF upsampled DINOv2 multi-scale feature를 back-project | dense high-res condition을 비교적 저비용으로 사용 |

### 6. Implementation idea

Pixal3D의 구현 흐름은 다음처럼 정리할 수 있다.

1. Training data construction
   - TRELLIS-500K subset of Objaverse를 사용한다.
   - Mesh에 random object-centric rotation을 적용하고 frontal perspective에서 varying FoV/camera distance로 render한다.
   - Mesh를 watertight 처리하고 SDF를 계산한다.
   - canonical mesh 대신 rendered camera view와 정렬된 pixel-aligned sparse SDF/latent pair를 만든다.

2. Backbone
   - Direct3D-S2의 VAE와 DiT architecture를 기본으로 쓴다.
   - Dense stage는 coarse occupancy grid를 생성한다.
   - Sparse stage는 sparse voxel latent를 denoise하고 VAE decoder가 sparse SDF를 복원한다.
   - Marching Cubes로 final mesh를 만든다.

3. Back-projection condition
   - 입력 이미지에서 DINOv2-Large patch feature와 global token을 추출한다.
   - NAF upsampler로 DINOv2 patch token을 input resolution $518 \times 518$에 맞게 upsample하여 fine feature map을 얻는다.
   - 각 voxel center를 camera projection으로 image plane에 사영하고, 해당 위치에서 multi-scale feature를 bilinear sampling한다.
   - sampling된 feature를 3D feature volume으로 만들고 diffusion noise volume에 더한다.
   - global token은 보조 semantic guidance로 cross-attention에 넣는다.

4. Inference projection setting
   - 학습 때는 ground-truth camera intrinsics, distance, cube scale을 사용한다.
   - inference 때는 상대적으로 작은 FoV와 unit cube scale을 택하고, image corner ray가 unit cube의 back face vertex를 지나도록 camera distance를 계산한다.
   - 논문은 이 heuristic이 frustum information을 유지하면서 voxel utilization을 크게 희생하지 않는다고 보고한다.

5. Multi-view
   - known camera pose를 가정한다.
   - 각 view feature를 동일 3D volume에 back-project한다.
   - voxel별 feature를 단순 average로 aggregate한다.
   - view 수가 늘수록 observed surface가 늘어나 generative ambiguity가 줄어든다.

6. Scene generation
   - SAM3로 object mask를 얻고 Qwen-image-edit으로 occluded region을 2D completion한다.
   - completed object crop을 Pixal3D에 넣어 object mesh를 camera-aligned로 생성한다.
   - MoGe point map에서 global geometry cue를 얻는다.
   - Pixal3D output과 MoGe prediction 사이의 point-wise constraint를 만들고 least-squares로 object scale/depth를 추정한다.

### 7. Mathematical background

논문에서 수식 extraction은 일부 symbol이 누락되어 있지만, 방법의 수학적 골자는 pinhole projection과 feature lifting이다. voxel 또는 3D point $\mathbf{x}_c = (x, y, z)^\top$가 camera coordinate에 있을 때 image pixel은 다음 projection으로 대응된다.

$$
\tilde{\mathbf{u}} \sim K \mathbf{x}_c,\quad
\mathbf{u} = \left(\frac{\tilde{u}_x}{\tilde{u}_z}, \frac{\tilde{u}_y}{\tilde{u}_z}\right)
$$

여기서 $K$는 camera intrinsic matrix이고, $\mathbf{u}$는 image feature map에서 sampling할 위치다. DINOv2 feature map을 $F_s(\mathbf{u})$라고 하면 scale $s$별 feature를 bilinear sampling하고 평균하여 voxel condition을 만든다.

$$
C(\mathbf{x}_c) = \frac{1}{S}\sum_{s=1}^{S} \operatorname{BilinearSample}(F_s, \mathbf{u})
$$

이렇게 얻은 $C(\mathbf{x}_c)$는 diffusion noise volume과 같은 spatial grid에 놓이므로, cross-attention key/value를 통해 간접적으로 condition하는 대신 noise/latent feature에 직접 더할 수 있다.

$$
\epsilon_t'(\mathbf{x}_c) = \epsilon_t(\mathbf{x}_c) + \phi(C(\mathbf{x}_c))
$$

$\phi$는 channel alignment를 위한 projection으로 볼 수 있다. 논문의 관점에서 핵심은 이 연산이 "어느 pixel이 어느 3D location에 영향을 주는가"를 attention이 학습해서 찾게 하지 않고, camera geometry가 미리 정해준다는 점이다. Multi-view에서는 view $i$마다 $C_i(\mathbf{x}_c)$를 만들고 평균한다.

$$
C_{\text{mv}}(\mathbf{x}_c) = \frac{1}{N}\sum_{i=1}^{N} C_i(\mathbf{x}_c)
$$

이 formulation은 occlusion-aware visibility weighting이나 learned fusion을 쓰지 않는 단순 평균이라는 한계가 있지만, 논문은 이 단순함만으로도 Toys4K multi-view 실험에서 큰 성능 차이를 얻는다.

### 8. Experiments

**Single-view on Toys4K**

Toys4K 전체 mesh에 대해 generated mesh의 surface normal을 입력 이미지 coordinate frame에서 render하고 ground-truth normal map과 비교한다. Metric은 IoU, PSNR, SSIM, LPIPS, mean/median angular error, boundary mean angular error, threshold accuracy다. Pixal3D는 모든 metric에서 baseline을 앞선다.

| Method | IoU | PSNR | SSIM | LPIPS | Mean | Median | Mean_B | 11.25 | 22.5 | 30 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| TRELLIS | 79.48 | 20.98 | 0.883 | 0.204 | 25.00 | 17.97 | 36.04 | 46.82 | 63.99 | 70.80 |
| TripoSG | 73.54 | 19.73 | 0.873 | 0.250 | 28.55 | 21.20 | 41.71 | 39.85 | 57.18 | 64.81 |
| Hunyuan3D-2.1 | 83.33 | 21.96 | 0.889 | 0.179 | 21.19 | 14.05 | 32.46 | 51.37 | 69.08 | 75.83 |
| Direct3D-S2 | 74.23 | 19.49 | 0.851 | 0.268 | 29.99 | 23.46 | 41.04 | 37.56 | 55.46 | 63.20 |
| Pixal3D | 93.57 | 24.21 | 0.897 | 0.108 | 16.63 | 11.77 | 21.80 | 53.13 | 77.96 | 85.35 |

**In-the-wild single-view**

저자들은 Internet/AI-generated source에서 150장의 complex image를 추가로 수집한다. Ground-truth camera pose나 normal map이 없기 때문에 Uni3D, ULIP2 기반 image-3D consistency와 30명 user study를 사용한다. Pixal3D는 Uni3D 42.11, ULIP2 45.04, fidelity 4.91, quality 4.74로 가장 높다. 특히 user study fidelity score가 Direct3D-S2 3.21보다 크게 높아, 정량 embedding metric보다 사람이 보는 pixel-level consistency에서 차이가 더 크게 나타난다.

| Method | Uni3D | ULIP2 | Fidelity | Quality |
|---|---:|---:|---:|---:|
| TRELLIS | 41.09 | 44.76 | 1.86 | 1.99 |
| TripoSG | 40.99 | 44.64 | 2.25 | 2.14 |
| Hunyuan3D-2.1 | 41.15 | 44.65 | 2.77 | 2.50 |
| Direct3D-S2 | 41.62 | 44.79 | 3.21 | 3.64 |
| Pixal3D | 42.11 | 45.04 | 4.91 | 4.74 |

**Multi-view on Toys4K**

Baselines는 VGGT와 TRELLIS multi-view version이다. Metric은 Chamfer Distance, Earth Mover's Distance, F-Score이며 view 수를 2, 4, 6으로 바꿔 평가한다.

| Method | View | CD $\times 10^{-4}$ | EMD $\times 10^{-2}$ | F-Score |
|---|---:|---:|---:|---:|
| VGGT | 2 | 613.55 | 19.60 | 9.57 |
| TRELLIS | 2 | 21.39 | 2.40 | 43.68 |
| Pixal3D | 2 | 5.27 | 1.13 | 64.94 |
| VGGT | 4 | 881.53 | 21.71 | 10.25 |
| TRELLIS | 4 | 18.35 | 2.19 | 45.90 |
| Pixal3D | 4 | 4.73 | 1.05 | 67.85 |
| VGGT | 6 | 2791.10 | 25.33 | 9.67 |
| TRELLIS | 6 | 18.13 | 2.16 | 46.02 |
| Pixal3D | 6 | 4.16 | 1.00 | 69.04 |

VGGT가 point cloud reconstruction에서 floaters/outliers를 만들고 TRELLIS가 smooth mesh를 만들지만 multi-view fidelity가 제한되는 반면, Pixal3D는 view-aligned feature aggregation으로 cross-view consistency가 좋아진다고 설명한다.

**Ablation**

Feature upsampling을 제거하면 DINOv2의 coarse patch token, 예를 들어 $37 \times 37$ token만 써야 해서 fine detail과 alignment가 떨어진다. Back-projection condition을 제거하고 conventional cross-attention으로 바꾸면 pixel-aligned 3D generator의 training convergence가 느리고 불안정하며 fidelity가 낮아진다. 따라서 novelty는 pixel-aligned target만이 아니라 target representation과 back-projection conditioner의 결합에 있다.

### 9. Limitations and future work

논문이 직접 언급한 limitation은 세 가지다.

- Pixel-level noise sensitivity: segmentation boundary 같은 작은 noise가 back-projection을 통해 3D artifact로 증폭될 수 있다.
- Multi-view camera pose assumption: current multi-view formulation은 known and reasonably accurate camera pose를 가정한다. 로봇 현장에서는 pose estimation error, rolling shutter, calibration drift가 fidelity를 깎을 수 있다.
- Scene pipeline dependency on 2D inpainting: occluded region completion을 Qwen-image-edit에 의존하므로 complex occlusion에서는 잘못된 geometry prior가 들어갈 수 있다.

논문이 제시한 future work는 texture/material synthesis, 2D pixel manipulation 기반 downstream 3D editing, video-based 3D scene generation이다. Robotics 관점에서 추가로 중요한 open question은 다음과 같다.

- Metric scale: generated object가 실제 물체 크기와 어떻게 calibrate되는지 명확하지 않다.
- Physical validity: watertightness, self-intersection, thin structure robustness, contact-stable mesh 여부가 motion planning/simulation 기준으로 평가되지 않았다.
- Dynamic/articulated objects: 현재 formulation은 rigid object/scene asset 중심이다.
- Visibility fusion: multi-view aggregation이 단순 average라 occlusion reasoning, view confidence weighting, specular/transparent object handling은 약할 수 있다.
- Real sensor noise: in-the-wild 이미지는 쓰지만 robot RGB-D noise, motion blur, segmentation error, pose graph drift에 대한 stress test는 없다.

### 10. 결론

Pixal3D는 "3D generation이 입력 이미지를 닮긴 하지만 pixel-level fidelity가 낮다"는 문제를 2D-3D correspondence의 문제로 재해석한다. Canonical space와 cross-attention을 중심으로 한 기존 generator는 image feature가 3D 어디에 작용해야 하는지 암묵적으로 학습해야 하지만, Pixal3D는 input camera frame에 정렬된 3D latent와 back-projected feature volume으로 이 대응을 명시화한다.

실험적으로는 single-view Toys4K normal metric, in-the-wild user study, multi-view CD/EMD/F-Score에서 강한 결과를 보인다. 특히 같은 Direct3D-S2 backbone을 바탕으로 conditioning만 바꾼 비교가 설득력 있다. 다만 논문은 geometry fidelity 중심의 evidence가 강하고, robotics deployment에 필요한 physical validity, metric scale, closed-loop perception, real sensor robustness는 아직 별도 검증이 필요하다.

한 줄로 요약하면, Pixal3D는 3D generation을 "canonical object prior"에서 "camera-aligned generative reconstruction"으로 옮겨 놓는 논문이며, 로봇 시각에서는 observation-aligned mesh asset을 만드는 방향으로 꽤 실용적인 힌트를 준다.

## 추가 질문과 답변
