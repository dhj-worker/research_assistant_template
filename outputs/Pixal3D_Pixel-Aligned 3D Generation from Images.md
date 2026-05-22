# Pixal3D: Pixel-Aligned 3D Generation from Images

저자: Dong-Yang Li, Wang Zhao, Yuxin Chen, Wenbo Hu, Meng-Hao Guo, Fang-Lue Zhang, Ying Shan, Shi-Min Hu  
Venue/상태: SIGGRAPH 2026, arXiv:2605.10922  
작업 기준: 로컬 PDF `papers/Pixal3D_Pixel-Aligned 3D Generation from Images.pdf`와 공개 arXiv/프로젝트 페이지를 기준으로 정리.

## Abstract

Recent advances in 3D generative models have rapidly improved image-to-3D synthesis quality, enabling higher-resolution geometry and more realistic appearance.

**최근 3D 생성 모델의 발전은 image-to-3D 합성 품질을 빠르게 끌어올려, 더 높은 해상도의 기하와 더 사실적인 외형을 가능하게 했다.**

Yet fidelity, which measures pixel-level faithfulness of the generated 3D asset to the input image, still remains a central bottleneck.

**그러나 생성된 3D asset이 입력 이미지에 대해 픽셀 수준으로 얼마나 충실한지를 뜻하는 fidelity는 여전히 핵심 병목으로 남아 있다.**

We argue this stems from an implicit 2D-3D correspondence issue: most 3D-native generators synthesize shape in canonical space and inject image cues via attention, leaving pixel-to-3D associations ambiguous.

**저자들은 이 문제가 암묵적인 2D-3D 대응 문제에서 비롯된다고 주장한다. 대부분의 3D-native generator는 canonical space에서 형상을 합성하고 attention으로 이미지 단서를 주입하기 때문에, pixel-to-3D association이 모호하게 남는다.**

To tackle this issue, we draw inspiration from 3D reconstruction and propose Pixal3D, a pixel-aligned 3D generation paradigm for high-fidelity 3D asset creation from images.

**이를 해결하기 위해 저자들은 3D reconstruction에서 영감을 받아, 이미지로부터 high-fidelity 3D asset을 만들기 위한 pixel-aligned 3D generation paradigm인 Pixal3D를 제안한다.**

Instead of generating in a canonical pose, Pixal3D directly generates 3D in a pixel-aligned way, consistent with the input view.

**Pixal3D는 canonical pose에서 생성하는 대신, 입력 view와 일관된 pixel-aligned 방식으로 3D를 직접 생성한다.**

To enable this, we introduce a pixel back-projection conditioning scheme that explicitly lifts multi-scale image features into a 3D feature volume, establishing direct pixel-to-3D correspondence without ambiguity.

**이를 가능하게 하기 위해, 저자들은 multi-scale image feature를 3D feature volume으로 명시적으로 lift하는 pixel back-projection conditioning scheme을 도입하여 모호성 없는 직접적인 pixel-to-3D correspondence를 만든다.**

We show that Pixal3D is not only scalable and capable of producing high-quality 3D assets, but also substantially improves fidelity, approaching the fidelity level of reconstruction.

**Pixal3D는 확장 가능하고 고품질 3D asset을 생성할 수 있을 뿐 아니라, reconstruction 수준에 가까운 fidelity까지 크게 향상함을 보인다.**

Furthermore, Pixal3D naturally extends to multi-view generation by aggregating back-projected feature volumes across views.

**또한 Pixal3D는 여러 view에서 back-projected feature volume을 aggregation함으로써 multi-view generation으로 자연스럽게 확장된다.**

Finally, we show pixel-aligned generation benefits scene synthesis, and present a modular pipeline that produces high-fidelity, object-separated 3D scenes from images.

**마지막으로 pixel-aligned generation이 scene synthesis에도 이점을 주며, 이미지로부터 high-fidelity의 object-separated 3D scene을 만드는 modular pipeline을 제시한다.**

Pixal3D for the first time demonstrates 3D-native pixel-aligned generation at scale, and provides a new inspiring way towards high-fidelity 3D generation of object or scene from single or multi-view images.

**Pixal3D는 대규모 3D-native pixel-aligned generation을 처음으로 보여주며, single-view 또는 multi-view 이미지로부터 object나 scene을 high-fidelity 3D로 생성하는 새로운 방향을 제시한다.**

## 목차

PDF outline metadata를 직접 추출하지는 못했으므로, 논문 본문 구조와 공식 프로젝트 페이지/공개 요약의 heading을 기준으로 추정한 목차이다. 다시 검토한 결과, 논문의 논리 전개는 아래 구조와 일치한다.

1. Introduction
2. Related Work
   - 3D generative models
   - Image-to-3D generation and reconstruction
   - Pixel-aligned representations / reconstruction-style conditioning
3. Method
   - Pixel-aligned generation paradigm
   - Pixel-aligned structured latent representation learning
   - Image back-projection-based conditioner
   - Two-stage / cascade 3D generative process
   - Multi-view extension
   - Scene generation pipeline
4. Experiments
   - Single-view generation
   - Multi-view generation
   - In-the-wild qualitative comparison
   - Scene synthesis
   - User study
   - Ablation studies
5. Limitations and Future Work
6. Conclusion

## 요약

### 1. 논문이 겨냥하는 병목

이 논문의 핵심 문제의식은 image-to-3D에서 흔히 말하는 "quality"와 "fidelity"를 분리해서 보는 데 있다.

- Quality: 결과 3D asset 자체가 그럴듯하고 고해상도이며 완성된 형상인가.
- Fidelity: 입력 이미지에 보이는 실루엣, 구조, 세부 파트, 표면 방향, photometric/detail cue가 3D 결과에 픽셀 수준으로 반영되는가.

최근 TRELLIS, TripoSG, Hunyuan3D, Direct3D-S2 계열은 3D asset 품질을 크게 끌어올렸지만, 대부분 canonical coordinate에서 object를 생성한다. 입력 이미지는 cross-attention 또는 global/image token 형태로 주입된다. 이때 이미지의 특정 pixel feature가 3D 공간의 어느 위치, 어느 depth, 어느 surface element에 대응되는지가 구조적으로 보장되지 않는다.

Pixal3D의 주장은 명확하다. 고충실도 image-to-3D의 병목은 generator capacity만의 문제가 아니라, conditioning geometry가 잘못 잡힌 문제다. 따라서 learned attention에 2D-3D 대응을 맡기지 말고, camera geometry를 이용해 이미지 feature를 3D volume으로 직접 back-project해야 한다.

### 2. 전체 연결 구조

논문은 reconstruction과 generation의 장점을 결합하는 식으로 전개된다.

1. Reconstruction은 관측된 view에 대한 pixel-level correspondence가 강하지만, occluded region이나 unseen backside completion에는 약하다.
2. 3D generative model은 complete asset을 만들 수 있지만, 입력 이미지에 보이는 세부와 3D surface의 대응이 느슨하다.
3. Pixal3D는 입력 camera frame에 aligned된 3D latent를 생성하고, image feature를 voxel/ray geometry에 따라 3D conditioning volume으로 lift한다.
4. 이렇게 만든 조건부 3D diffusion이 visible region에서는 reconstruction-like fidelity를 유지하고, invisible region에서는 learned 3D prior로 plausible completion을 수행한다.

즉 논문의 구조는 `canonical generation의 fidelity 실패` -> `pixel-aligned coordinate로 재정의` -> `back-projection conditioner` -> `single/multi-view/scene 확장` -> `실험으로 fidelity 개선 검증`의 흐름이다.

### 3. 핵심 아이디어

#### 3.1 Canonical generation에서 pixel-aligned generation으로

기존 3D-native generator는 보통 object를 canonical pose의 latent space에서 생성한다. 이 방식은 dataset-level alignment에는 유리하지만, 입력 이미지의 camera/view와 결과 3D 사이에 pose alignment 문제가 생긴다. 이미지 feature를 cross-attention으로 넣어도 attention map은 soft association일 뿐, 특정 pixel ray와 3D voxel 사이의 geometric constraint를 강제하지 않는다.

Pixal3D는 3D asset을 입력 camera coordinate 또는 input-view-consistent coordinate에서 생성한다. 따라서 입력 이미지의 한 pixel은 camera ray를 정의하고, 이 ray가 통과하는 3D volume 위치에 해당 pixel/feature의 정보가 주입된다. visible surface의 위치는 여전히 생성 모델이 추론하지만, 적어도 "어떤 이미지 feature가 어느 ray상의 3D 후보들과 연결되는가"는 명시적으로 고정된다.

#### 3.2 Pixel back-projection conditioning

입력 이미지 \(I\)에서 DINOv2 등 image encoder로 multi-scale feature map \(\{F_l\}\)을 추출한다. 3D volume의 voxel center를 \(\mathbf{x}\)라고 하면, 카메라 intrinsics/extrinsics를 이용해 이를 이미지 평면으로 project한다.

$$
\tilde{\mathbf{u}} = K [R \mid \mathbf{t}] \tilde{\mathbf{x}},
\quad
\mathbf{u} = \pi(\tilde{\mathbf{u}})
$$

여기서 \(K\)는 intrinsic matrix, \(R,\mathbf{t}\)는 camera pose, \(\pi\)는 homogeneous projection이다. 각 scale \(l\)에서 \(\mathbf{u}\) 위치의 image feature를 bilinear sampling으로 가져오고, 이를 voxel feature로 쌓는다.

$$
\mathbf{c}(\mathbf{x}) =
\operatorname{Agg}_{l}
\left(
\operatorname{Sample}(F_l, \mathbf{u}_l)
\right)
$$

이렇게 얻은 \(\mathbf{c}(\mathbf{x})\)가 3D feature volume을 이루며, diffusion model의 noise volume 또는 sparse latent와 결합되어 conditioning signal이 된다. 중요한 점은 conditioning이 token-level attention이 아니라 voxel-wise geometric lookup이라는 것이다.

#### 3.3 Multi-scale feature와 high-frequency detail

논문은 fine detail 보존을 위해 multi-scale feature를 사용한다. 공개 자료 기준으로 DINOv2 feature와 NAF-style upsampling module이 언급된다. 의미적으로는 coarse semantic structure와 high-frequency local detail을 동시에 제공하려는 구성이다.

- 낮은 해상도 feature: object-level semantics, part layout, global shape prior
- 높은 해상도 feature: edge, small part, pattern, thin geometry, normal detail
- voxel-wise aggregation: 각 3D 위치가 해당 pixel/ray에서 나온 feature를 직접 받음

이 설계 때문에 키보드 layout, face detail, 꽃잎 같은 작은 구조에서 기존 canonical generator보다 fidelity가 높아진다고 해석할 수 있다.

#### 3.4 Pixel-aligned structured latent representation

Pixal3D는 Direct3D-S2 계열의 sparse voxel latent / structured 3D latent diffusion backbone을 기반으로 한다. 다만 VAE가 canonical object를 압축하는 것이 아니라, pixel-aligned sparse SDF를 압축하도록 학습된다.

개념적으로는 다음 흐름이다.

1. mesh를 input-view-aligned coordinate로 배치한다.
2. 이를 sparse SDF 또는 occupancy/voxel latent로 변환한다.
3. VAE encoder가 pixel-aligned sparse SDF를 compact latent로 압축한다.
4. diffusion/flow transformer가 image back-projection conditioning을 받아 latent를 생성한다.
5. VAE decoder와 Marching Cubes 계열 절차로 mesh를 복원한다.

공식 모델 카드의 최신 구현은 TRELLIS.2 backbone 기반 개선판을 제공하지만, 논문 결과 재현에는 `paper` branch의 Direct3D-S2 기반 구현을 사용하라고 명시되어 있다.

### 4. 기존 방법과의 비교

| 방법 계열 | 좌표계/생성 방식 | 이미지 조건 주입 | 장점 | Pixal3D 관점의 한계 |
|---|---|---|---|---|
| TRELLIS / TRELLIS.2 | 3D latent 기반 고품질 asset 생성 | image feature 또는 attention 기반 조건 | 강한 asset prior, 실용적 품질 | pixel-to-3D correspondence가 명시적으로 강제되지 않음 |
| TripoSG | single-image 3D 생성 | learned image conditioning | 빠른 feed-forward 생성과 좋은 shape prior | 입력 view의 세부 구조 보존이 attention/latent에 의존 |
| Hunyuan3D-2.1 / HY3D | image-to-3D asset 생성 | image-conditioned generation | 텍스처/asset 품질이 높음 | canonical 또는 view-agnostic 처리에서 alignment ambiguity 발생 가능 |
| Direct3D-S2 | structured 3D latent diffusion | image condition + 3D latent generation | Pixal3D의 강한 backbone | 원래 방식만으로는 pixel-aligned conditioning이 부족 |
| Reconstruction/MVS/SfM | camera geometry 기반 2D-3D 대응 | feature matching, triangulation, optimization | visible surface fidelity가 강함 | single-view completion과 generative plausibility가 약함 |
| Pixal3D | input-view-aligned 3D generation | geometric back-projection conditioning | reconstruction-like fidelity와 generative completion 결합 | camera/crop/noise/occlusion 조건에 민감할 수 있음 |

### 5. Multi-view 확장

Pixal3D의 multi-view 확장은 구조적으로 단순하다. 각 view \(i\)에 대해 독립적으로 feature volume \(\mathbf{c}_i(\mathbf{x})\)를 만들고, voxel 단위로 aggregate한다.

$$
\begin{aligned}
\mathbf{c}_{\mathrm{mv}}(\mathbf{x})
&= \frac{1}{N}
\sum_{i=1}^{N}
\mathbf{c}_i(\mathbf{x})
\end{aligned}
$$

공개 요약에서는 simple averaging이 언급된다. 이 단순한 aggregation이 가능한 이유는 모든 view의 feature가 같은 3D voxel coordinate로 back-project되기 때문이다. view 수가 늘수록 한 ray만으로는 해결하기 어려운 depth ambiguity가 줄고, 다른 view의 관측이 surface localization을 더 강하게 제약한다.

다만 이 장점은 multi-view camera pose가 알려져 있거나 충분히 정확하다는 조건에 의존한다. pose error가 있으면 voxel feature aggregation이 blur 또는 conflict를 만들 수 있다.

### 6. Scene synthesis pipeline

Pixal3D는 단일 object를 넘어 scene synthesis에도 확장된다. 공개 리뷰 자료를 기준으로 pipeline은 다음처럼 해석된다.

1. 입력 scene image에서 SAM3 등으로 object segmentation을 수행한다.
2. occlusion이 있는 object crop은 Qwen-image-edit 같은 2D completion/inpainting으로 보완한다.
3. 각 object image를 Pixal3D에 넣어 pixel-aligned 3D asset을 생성한다.
4. MoGe 같은 global point-map predictor로 scene-level depth/point map을 얻는다.
5. Pixal3D output과 scene point map 사이의 pixel-wise constraint를 이용해 object별 scale/depth를 least-squares로 추정한다.
6. object-separated 3D scene으로 조립한다.

핵심은 object pose를 일반적인 7-DoF alignment 문제로 풀지 않아도 된다는 점이다. 각 object가 이미 input view에 aligned되어 있으므로, 상대 scale과 depth 중심의 정렬 문제로 단순화된다. robotics 관점에서는 scene decomposition, object-centric digital twin, manipulation target assetization에 특히 유용한 설계다.

### 7. 실험 결과 해석

#### 7.1 Single-view

Toys4K single-view 평가에서 Pixal3D는 TRELLIS, TripoSG, Hunyuan3D-2.1, Direct3D-S2 대비 rendered normal map 기반 지표에서 우수하다고 보고된다. 공개 리뷰 자료에 따르면 예시 수치는 다음과 같다.

- Pixal3D: IoU \(93.57\), PSNR \(24.21\), SSIM \(0.897\), LPIPS \(0.108\)
- Direct3D-S2: IoU \(74.23\), PSNR \(19.49\)

이 결과는 단순히 mesh가 그럴듯하다는 의미보다, 입력 view에서의 normal/rendered evidence가 ground truth와 더 잘 맞는다는 의미가 크다. 즉 논문 제목의 pixel-aligned fidelity 주장을 직접 지지한다.

#### 7.2 In-the-wild qualitative/user study

in-the-wild 이미지에서는 정량 ground truth가 제한적이므로 Uni3D/ULIP2 같은 image-3D consistency metric과 user study를 함께 사용한 것으로 정리된다. 질적 비교에서는 Pixal3D가 keyboard layout, facial detail, 복잡한 small structure 등에서 더 입력 이미지에 가까운 결과를 보인다고 보고된다.

#### 7.3 Multi-view

Multi-view Toys4K 평가에서는 view 수가 \(2,4,6\)으로 증가할수록 Chamfer Distance, EMD, F-Score가 개선되는 경향이 언급된다. 공개 리뷰 자료의 예로 6-view에서 Pixal3D의 Chamfer Distance가 \(4.16 \times 10^{-4}\), TRELLIS가 \(18.13 \times 10^{-4}\)로 보고된다.

이 결과는 back-projected feature volume aggregation이 단순한 heuristic이 아니라 실제로 multi-view evidence를 geometry에 누적하는 역할을 한다는 증거다.

#### 7.4 Ablation

Ablation의 핵심 메시지는 두 가지다.

- Back-projection conditioning을 제거하거나 cross-attention 기반으로 대체하면 fidelity와 안정성이 떨어진다.
- Multi-scale feature upsampling이 없으면 high-frequency detail 보존이 약해진다.

즉 성능 향상은 backbone 크기만의 효과라기보다, pixel-aligned coordinate와 explicit projection conditioner라는 구조적 선택에서 온다.

### 8. Robotics 관점의 novelty와 relevance

Robotics에서 이 논문이 중요한 이유는 image-conditioned 3D asset generation을 단순 콘텐츠 생성이 아니라 perception-to-geometry 변환 문제로 다시 묶기 때문이다.

- Manipulation: 단일 RGB 이미지에서 object mesh를 만들 때, visible surface와 input pixel의 정렬이 좋아야 grasp point, contact geometry, affordance region을 신뢰할 수 있다.
- Simulation/digital twin: real image에서 sim-ready object를 만들 때 canonical generator의 hallucination보다 reconstruction-like visible fidelity가 중요하다.
- Scene understanding: object-separated scene reconstruction은 cluttered tabletop, indoor scene parsing, rearrangement planning과 연결된다.
- AR/VR/teleoperation: camera view와 결과 3D가 잘 맞으면 operator가 본 이미지와 생성 asset 사이의 cognitive mismatch가 줄어든다.
- Data generation: robot learning용 synthetic asset을 만들 때 입력 exemplar의 세부 형상이 유지되면 sim-to-real gap을 줄이는 데 유리하다.

특히 Pixal3D는 "이미지 feature를 3D prior에 넣는다"가 아니라 "camera geometry를 통해 feature의 위치를 먼저 정한다"는 점에서 robotics perception의 inductive bias와 잘 맞는다.

### 9. 한계와 향후 연구

1. Single-view depth ambiguity  
   같은 pixel feature가 ray상의 여러 depth 후보에 복제되므로, 실제 surface depth는 여전히 generative prior가 결정한다. depth/normal/point-map prior를 함께 넣으면 ambiguity를 줄일 수 있다.

2. Camera parameter sensitivity  
   in-the-wild single image에서는 정확한 intrinsics, crop, FoV, object scale을 알기 어렵다. heuristic camera placement가 crop이나 lens distortion에 민감할 수 있다.

3. Multi-view pose dependency  
   multi-view aggregation은 pose가 정확할 때 강하다. SfM/pose estimation error가 있는 실제 robotics setting에서는 robust aggregation이나 pose refinement가 필요하다.

4. Thin/open structure 표현 한계  
   sparse SDF와 Marching Cubes 계열은 thin part, open surface, topology 복잡도가 큰 구조에서 한계가 있을 수 있다.

5. Texture/material fidelity  
   공개 모델 카드에서는 PBR texture generation까지 언급되지만, 논문 핵심은 geometry/pixel alignment에 더 가깝다. material/BRDF까지 pixel-aligned로 제약하는 연구가 후속으로 필요하다.

6. Scene pipeline의 modular error accumulation  
   segmentation, inpainting, object generation, point-map alignment가 분리되어 있어 각 단계 오류가 누적될 수 있다. end-to-end scene-level training은 아직 열려 있다.

### 10. 결론

Pixal3D의 가장 큰 기여는 image-to-3D generation에서 fidelity 문제를 "더 큰 generator" 문제가 아니라 "2D-3D correspondence를 어떻게 구조화할 것인가"의 문제로 재정의한 점이다. 입력 view와 aligned된 3D latent를 생성하고, image feature를 back-projection으로 3D feature volume에 직접 배치함으로써, reconstruction-like visible fidelity와 generative completion을 동시에 노린다.

논문은 single-view, multi-view, scene generation까지 같은 pixel-aligned principle로 연결하며, 3D-native generation이 reconstruction의 geometry discipline을 흡수하는 방향을 설득력 있게 보여준다.

## 참고한 공개 자료

- arXiv: https://arxiv.org/abs/2605.10922
- Project page: https://ldyang694.github.io/projects/pixal3d/
- Hugging Face model card: https://huggingface.co/TencentARC/Pixal3D
- Literature review 참고: https://www.themoonlight.io/en/review/pixal3d-pixel-aligned-3d-generation-from-images

## 추가 질문과 답변
