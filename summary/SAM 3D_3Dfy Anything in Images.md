# SAM 3D: 3Dfy Anything in Images

## 메타데이터

- PDF 파일: `SAM 3D_3Dfy Anything in Images.pdf`
- 논문 제목: SAM 3D: 3Dfy Anything in Images
- 저자: SAM 3D Team, Xingyu Chen, Fu-Jen Chu, Pierre Gleize, Kevin J Liang, Alexander Sax, Hao Tang, Weiyao Wang, Michelle Guo, Thibaut Hardin, Xiang Li, Aohan Lin, Jiawei Liu, Ziqi Ma, Anushka Sagar, Bowen Song, Xiaodong Wang, Jianing Yang, Bowen Zhang, Piotr Dollár, Georgia Gkioxari, Matt Feiszli, Jitendra Malik
- 소속: Meta Superintelligence Labs
- venue/arXiv: 확인 필요
- 연도: 확인 필요
- DOI/URL: Demo https://www.aidemos.meta.com/segment-anything/editor/convert-image-to-3d, Code https://github.com/facebookresearch/sam-3d-objects, Website https://ai.meta.com/sam3d
- 작업 일시: 2026-05-22 17:10

## Abstract

We present SAM 3D, a generative model for visually grounded 3D object reconstruction, predicting geometry, texture, and layout from a single image.

**SAM 3D는 단일 이미지로부터 geometry, texture, layout을 예측하는 visually grounded 3D object reconstruction용 generative model이다.**

SAM 3D excels in natural images, where occlusion and scene clutter are common and visual recognition cues from context play a larger role.

**SAM 3D는 occlusion과 scene clutter가 흔하고, context에서 얻는 visual recognition cue가 더 큰 역할을 하는 natural image 환경에서 강점을 보인다.**

We achieve this with a human- and model-in-the-loop pipeline for annotating object shape, texture, and pose, providing visually grounded 3D reconstruction data at unprecedented scale.

**저자들은 object shape, texture, pose를 annotation하기 위한 human- and model-in-the-loop pipeline을 통해 이를 달성하며, 전례 없는 규모의 visually grounded 3D reconstruction data를 제공한다.**

We learn from this data in a modern, multi-stage training framework that combines synthetic pretraining with real-world alignment, breaking the 3D "data barrier".

**이 데이터로부터 synthetic pretraining과 real-world alignment를 결합한 modern multi-stage training framework로 학습하여 3D의 "data barrier"를 돌파한다.**

We obtain significant gains over recent work, with at least a 5 : 1 win rate in human preference tests on real-world objects and scenes.

**실제 object와 scene에 대한 human preference test에서 최소 $5:1$ win rate를 보이며, 최근 방법들 대비 큰 성능 향상을 얻는다.**

We will release our code and model weights, an online demo, and a new challenging benchmark for in-the-wild 3D object reconstruction.

**저자들은 code와 model weight, online demo, 그리고 in-the-wild 3D object reconstruction을 위한 새로운 challenging benchmark를 공개할 예정이다.**

## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 재검토했다.

1. Introduction
2. The SAM 3D Model
   1. Problem Formulation
   2. Architecture
3. Training SAM 3D
   1. Pre & Mid-Training: Building a Base Model
      1. Pretraining: Single Isolated 3D Assets
      2. Mid-Training: Semi-Synthetic Capabilities
   2. Post-Training: Real-World Alignment
      1. Post-Training: Collection Step
      2. Post-Training: Model Improvement Step
4. Experiments
   1. Comparison with SOTA
   2. Analysis Studies
5. Related Work
6. Conclusion
7. Appendix
   1. Data Annotation Engine Details
   2. Pretraining and Mid-Training Data
   3. Details on Model Training
   4. Evaluations
   5. Additional Ablations
   6. Limitations

## 요약

### 1. 전체 구조

이 논문은 SAM 3D를 단순한 image-to-3D asset generator가 아니라, 자연 이미지 속 object instance를 mask 기준으로 선택하고 해당 object의 full 3D shape, texture, camera-relative layout까지 복원하는 foundation model로 제시한다. 핵심 문제의식은 기존 single-view 3D generation이 isolated object render 중심으로 학습되어 real-world clutter, occlusion, scale, pose, context cue를 충분히 다루지 못한다는 점이다.

논문은 크게 세 층으로 구성된다.

- 모델: Geometry model과 Texture & Refinement model의 two-stage latent flow matching 구조.
- 데이터 엔진: synthetic pretraining, semi-synthetic render-paste mid-training, real-world MITL/artist post-training.
- 평가: SA-3DAO benchmark, ISO3D, Aria Digital Twin, preference set에서 shape, texture, layout, scene reconstruction을 평가.

논문에서 가장 중요한 주장은 "recognition enables reconstruction"이다. 단일 이미지는 geometric signal만으로는 underdetermined이지만, object identity, scene context, familiar part prior, mask cue가 결합되면 plausible full 3D reconstruction을 생성할 수 있다는 관점이다.

### 2. Section 간 연결

Introduction은 single-view 3D perception의 고전적 pictorial cue 논의를 foundation model 관점으로 끌어온다. 2D image와 mask로부터 shape, texture, pose를 예측하려면 real-world paired 3D data가 필요하지만, 사람이 직접 3D mesh를 만드는 annotation은 scale이 맞지 않는다. 이 병목이 이후 데이터 엔진 설계의 동기가 된다.

Section 2는 이 문제를 조건부 생성 문제로 정식화한다. 입력은 image $I$와 object mask $M$이고, 출력은 shape $S$, texture $T$, rotation $R$, translation $t$, scale $s$이다. Geometry model은 coarse shape와 layout을 먼저 예측하고, Texture & Refinement model은 coarse shape를 기반으로 geometry detail과 texture를 보강한다.

Section 3은 모델보다 더 중요한 contribution인 training/data recipe를 설명한다. Iso-3DO synthetic isolated object pretraining으로 shape/texture vocabulary를 만들고, RP-3DO render-paste mid-training으로 mask-following, occlusion robustness, layout estimation을 주입한다. 이후 MITL-3DO와 Art-3DO를 통해 real-world domain gap을 줄이고, preference data로 DPO alignment를 수행한다.

Section 4는 이 recipe가 실제로 작동한다는 증거를 제시한다. SA-3DAO에서는 artist-created 3D ground truth를 사용해 real-world shape accuracy를 측정하고, ADT에서는 layout estimation을 평가한다. Table 4와 appendix ablation은 각 training stage가 누적적으로 성능에 기여함을 보여준다.

### 3. 핵심 주장과 근거

핵심 주장 1: SAM 3D는 natural image의 clutter와 occlusion에서도 object-level 3D shape, texture, layout을 jointly 복원한다.

- 근거: full image와 cropped object를 모두 DINOv2로 encode한다. crop은 target object detail을 제공하고, full image는 global scene context와 recognition cue를 제공한다.
- 결과: SA-3DAO shape metric에서 SAM 3D는 F1@0.01 $0.2344$, vIoU $0.2311$, Chamfer $0.0400$, EMD $0.1211$로 모든 비교 방법보다 우수하다.

핵심 주장 2: real-world 3D data barrier는 human 직접 제작이 아니라 "human selects/alignment + model proposals" 방식으로 우회할 수 있다.

- Stage 1은 image/object mask를 수집한다.
- Stage 2는 retrieval, text-to-3D, image-to-3D, SAM 3D checkpoint가 만든 $N$개 후보 중 annotator가 best candidate를 선택하게 한다.
- Stage 2.5는 model suite가 실패한 hard case를 3D artist에게 보낸다.
- Stage 3은 선택된 mesh를 2.5D point cloud에 맞춰 rotation, translation, scale로 align한다.
- 전체 수집 규모는 약 360K images, 850K unique object instances, 3.14M trainable shapes, 1.23M layout samples, 100K trainable textures, 7M+ pairwise preferences이다.

핵심 주장 3: synthetic pretraining만으로는 부족하고, LLM-style staged training과 preference alignment가 real-world 3D perception을 만든다.

- Iso-3DO pretraining: 2.7M meshes, 24 views, 2.5T training tokens.
- RP-3DO mid-training: 61M samples, 2.8M unique meshes, 2.7T training tokens.
- Post-training: MITL/Art-3DO SFT와 DPO, 최종 post-training iteration은 0.5T tokens.
- Table 4에서 Pre-training F1@0.01 $0.1349$가 최종 SAM 3D $0.2344$까지 상승한다.

### 4. Robotics 관점의 novelty와 relevance

Robotics 관점에서 SAM 3D의 의미는 "single RGB image 또는 RGB+pointmap에서 object-centric 3D asset과 pose proposal을 동시에 생성하는 perception prior"로 볼 수 있다는 점이다. 기존 pose estimation pipeline은 CAD model, known object category, tabletop/indoor constraint, multi-view/depth constraint에 기대는 경우가 많다. SAM 3D는 open-world object mask가 주어졌을 때 shape prior와 layout을 함께 생성하므로, manipulation, scene understanding, simulation asset bootstrapping, AR/robot digital twin 생성에 직접적인 relevance가 있다.

특히 pointmap conditioning은 robotics integration point다. 논문은 pointmap을 LiDAR 같은 hardware sensor나 monocular depth estimator에서 얻을 수 있다고 설명한다. shape quality 자체는 pointmap conditioning 여부에 크게 의존하지 않았지만, layout 평가에는 depth/pointmap이 중요하다. 따라서 실제 robot에서는 RGB-D camera, iPhone LiDAR, learned depth estimator와 결합해 pose/layout proposal을 만든 뒤, downstream grasp planning이나 scene graph에 넘기는 흐름이 자연스럽다.

다만 deployment에서는 그대로 쓰기 어렵다. SAM 3D는 object를 one-at-a-time으로 예측하며, contact, support, interpenetration, physical stability, co-planarity를 학습하지 않는다. 로봇 manipulation에서는 이런 물리 제약이 중요하므로, SAM 3D output은 final state estimator라기보다 rich proposal 또는 semantic-geometric prior로 쓰는 편이 안전하다.

### 5. 기존 방법과 비교

| 구분 | 기존 방법 | SAM 3D | 의미 |
|---|---|---|---|
| Image-to-3D asset generation | TRELLIS, Hunyuan3D, Direct3D-S2, TripoSG, Hi3DGen 등은 주로 isolated object나 cleaner image setting에서 강함 | cluttered real-world image와 mask 기반 target object를 다루며 shape, texture, layout을 함께 예측 | in-the-wild object reconstruction으로 문제 설정을 확장 |
| Scene reconstruction pipeline | HY3D/TRELLIS + MegaPose/FoundationPose 같은 pipeline은 shape generation과 pose estimation을 분리 | joint SAM 3D는 shape와 layout을 같은 model family에서 생성 | shape-layout mismatch를 줄이고 pose proposal 품질을 개선 |
| Pose/layout estimation | FoundationPose, MegaPose, render-and-compare 계열은 CAD/mesh proposal 품질과 initialization에 민감 | SAM 3D가 feedforward layout proposal을 만들고 필요하면 render-and-compare로 post-optimization 가능 | robotics pose pipeline의 proposal generator로 유용 |
| Real-world data | 기존 3D datasets는 synthetic object, indoor, tabletop, small-scale paired data에 치우침 | MITL-3DO, Art-3DO, SA-3DAO로 natural image paired 3D supervision을 확대 | real-world domain gap을 데이터 엔진으로 직접 다룸 |
| Alignment | 대부분 geometric/reconstruction loss 중심 | human preference 기반 DPO를 shape/texture에 적용 | symmetry, closure, floaters, bottomless mesh 같은 perceptual failure를 줄임 |

주요 정량 비교는 다음과 같다.

| 평가 | Metric | Best baseline | SAM 3D | 해석 |
|---|---:|---:|---:|---|
| SA-3DAO shape | F1@0.01 | Hi3DGen $0.1629$ | $0.2344$ | real-world artist GT 기준 shape accuracy가 크게 높음 |
| SA-3DAO shape | Chamfer | TripoSG $0.0844$ | $0.0400$ | 거리 기반 오류가 약 절반 수준 |
| SA-3DAO layout | 3D IoU | Pipeline HY3D-2.0 + FoundationPose $0.2937$ | $0.4254$ | joint layout generation이 pipeline보다 강함 |
| SA-3DAO layout | ADD-S @ 0.1 | Pipeline HY3D-2.0 + FoundationPose $0.5396$ | $0.7232$ | diameter-normalized pose/shape alignment 성공률 향상 |
| ADT layout | ADD-S @ 0.1 | Pipeline SAM 3D + FoundationPose $0.6495$ | $0.7673$ | SAM 3D shape를 쓰더라도 joint SAM 3D layout이 우수 |
| Texture preference | SAM 3D WR over TRELLIS on SA-3DAO | - | $86.2\%$ | 같은 SAM 3D shape 조건에서도 texture model 선호도가 높음 |

### 6. Implementation idea

입력은 image $I$와 object mask $M$이다. SAM 3D는 cropped object image/mask와 full image/mask를 각각 encode하여 네 종류의 conditioning token을 만든다. 여기서 cropped input은 target detail을, full input은 scene context와 object recognition cue를 제공한다. 선택적으로 pointmap $P$를 추가 conditioning으로 사용한다.

Geometry model은 다음 분포를 모델링한다.

$$
p(O, R, t, s \mid I, M)
$$

여기서 $O$는 coarse shape latent이고, $R$은 6D rotation representation, $t$는 translation, $s$는 scale이다. 논문은 약 1.2B parameter flow transformer와 Mixture-of-Transformers architecture를 사용한다. shape token과 layout token은 modality-specific projection을 거쳐 shared feature space로 들어가며, MoT attention mask를 통해 modality별 학습과 cross-modal information sharing을 동시에 허용한다.

Texture & Refinement model은 Geometry model이 예측한 active voxel을 받아 다음 분포를 모델링한다.

$$
p(S, T \mid I, M, O)
$$

이 model은 약 600M parameter sparse latent flow transformer이며, coarse geometry를 refine하고 texture를 생성한다. 최종 latent는 mesh decoder $D_m$ 또는 Gaussian splat decoder $D_g$로 decode될 수 있다.

추론 흐름은 다음처럼 정리할 수 있다.

1. object mask $M$으로 target object crop을 만든다.
2. DINOv2로 crop image/mask와 full image/mask를 encode한다.
3. optional pointmap $P$를 conditioning에 포함한다.
4. Geometry model이 coarse shape $O$와 layout $(R,t,s)$를 생성한다.
5. Texture & Refinement model이 $O$를 기반으로 high-resolution detail과 texture를 생성한다.
6. mesh 또는 Gaussian splat decoder로 3D asset을 출력한다.
7. 필요하면 layout을 render-and-compare 방식으로 post-optimization한다.

### 7. Mathematical background

문제 정식화는 단일 이미지 투영의 역문제를 조건부 분포 추정으로 둔다.

$$
p(S, T, R, t, s \mid I, M)
$$

모델의 목표는 이 분포를 근사하는 생성 모델 $q(S,T,R,t,s \mid I,M)$를 학습하는 것이다. 3D-to-2D projection은 lossy이므로, 결정론적 복원이 아니라 plausible distribution을 모델링하는 쪽이 자연스럽다.

Geometry model의 conditional rectified flow matching objective는 modality별 velocity field를 맞추는 형태다.

$$
L_{\mathrm{CFM}}
=
\sum_{m \in \mathcal{M}} \lambda_m
\mathbb{E}_{\tau, x_0^m}
\left[
\left\|
v_m - v_\theta^m(x_\tau^m, c, \tau)
\right\|_2^2
\right]
$$

여기서 $\mathcal{M} = \{S, R, t, s\}$, $c=(I,M)$, $x_0^m \sim \mathcal{N}(0,I)$, clean state $x_1^m$은 annotation에서 온 ground truth 3D modality이다. Linear interpolation path는 다음과 같다.

$$
x_\tau^m
=
\tau x_1^m + (1-\tau)x_0^m
$$

target velocity는 $v_m = x_1^m - x_0^m$이다. Texture & Refinement model도 SLAT feature 공간에서 유사한 flow matching objective를 사용한다.

DPO alignment는 같은 input $c$에 대해 선호된 3D output $x_w$와 덜 선호된 output $x_l$을 pair로 사용한다. 논문은 Diffusion-DPO를 flow matching에 맞게 적용해 learned velocity field와 frozen reference velocity field의 차이를 preference objective에 넣는다. 중요한 점은 DPO가 pure geometry metric이 포착하기 어려운 symmetry, closure, floaters, bottomless mesh 같은 human preference failure를 줄이는 데 쓰인다는 것이다.

Distillation은 shortcut model objective로 inference NFE를 줄인다. Geometry model은 기본 25 steps에서 4 steps로 줄여 sub-second shape/layout을 목표로 한다. robotics online perception에서는 이 distillation이 실제 latency 관점에서 중요하다.

### 8. Experiments

평가 데이터는 세 가지 축으로 나뉜다.

- SA-3DAO: natural image에서 3D artist가 만든 1K untextured object mesh benchmark. real-world 3D object reconstruction의 핵심 benchmark다.
- ISO3D: geometry GT가 없는 image-to-3D evaluation set으로, ULIP/Uni3D 같은 perceptual similarity를 사용한다.
- Aria Digital Twin: layout evaluation에 사용한다.
- Preference Set: MetaCLIP, SA-1B, LVIS 기반 curated real-world images에서 object-level/scene-level human preference를 측정한다.

Shape 결과에서 SAM 3D는 SA-3DAO 기준 모든 baseline을 앞선다. Table 2의 SAM 3D 수치는 F1@0.01 $0.2344$, vIoU $0.2311$, Chamfer $0.0400$, EMD $0.1211$이다. 같은 표에서 강한 baseline인 Hi3DGen도 F1@0.01 $0.1629$, vIoU $0.1531$에 머문다. 저자들은 human preference에서도 real images 기준 최소 $5:1$ head-to-head win rate를 보고한다.

Layout 결과는 robotics 측면에서 더 흥미롭다. Table 3에서 Joint SAM 3D는 SA-3DAO에서 3D IoU $0.4254$, ICP-Rot. $20.7667$, ADD-S $0.2661$, ADD-S @ 0.1 $0.7232$를 기록한다. ADT에서도 3D IoU $0.4970$, ICP-Rot. $15.2515$, ADD-S $0.0765$, ADD-S @ 0.1 $0.7673$이다. Pipeline SAM 3D + FoundationPose보다도 joint SAM 3D가 높아, shape만 좋은 것이 아니라 layout predictor 자체가 유용하다는 근거가 된다.

Training ablation은 staged recipe의 필요성을 잘 보여준다.

| Training stage | F1@0.01 | vIoU | Chamfer | EMD | Texture WR |
|---|---:|---:|---:|---:|---:|
| Pre-training (Iso-3DO) | $0.1349$ | $0.1202$ | $0.1036$ | $0.2396$ | - |
| + Mid-training (RP-3DO) | $0.1705$ | $0.1683$ | $0.0760$ | $0.1821$ | $60.7$ |
| + SFT (MITL-3DO) | $0.2027$ | $0.2025$ | $0.0578$ | $0.1510$ | $66.9$ |
| + DPO (MITL-3DO) | $0.2156$ | $0.2156$ | $0.0498$ | $0.1367$ | $66.4$ |
| + SFT (Art-3DO) | $0.2331$ | $0.2337$ | $0.0445$ | $0.1257$ | - |
| + DPO (Art-3DO) | $0.2344$ | $0.2311$ | $0.0400$ | $0.1211$ | - |

Appendix의 knockout도 같은 결론을 강화한다. Full SAM 3D의 F1@0.01은 $0.2344$인데, MITL-3DO를 제거하면 $0.2211$, Art-3DO를 제거하면 $0.2027$, MITL DPO를 제거하면 $0.2156$으로 떨어진다. 즉 real-world MITL와 artist data, preference alignment가 모두 필요하다.

### 9. Limitations and future work

논문이 명시한 주요 limitation은 세 가지다.

첫째, output resolution 제한이다. Geometry model은 coarse shape resolution $O \in \mathbb{R}^{64^3}$를 사용하며, Gaussian splat decoder도 occupied voxel당 최대 32 splats 수준이다. 일반 object에는 충분하지만, human body의 손/얼굴처럼 fine detail에 민감한 구조에서는 distortion이나 detail loss가 눈에 띌 수 있다. 저자들은 architecture change, superresolution, parts-based generation, implicit 3D representation이 자연스러운 다음 단계라고 본다.

둘째, layout은 object-wise independent prediction이다. SAM 3D는 multi-object physical interaction을 학습하지 않으므로 contact, stability, interpenetration, 같은 ground plane 위 정렬 같은 constraint를 보장하지 않는다. scene-level reconstruction 이미지는 그럴듯해도 robot planning에 그대로 투입하면 collision이나 support relation이 틀릴 수 있다.

셋째, texture prediction은 predicted pose를 모른 채 수행된다. rotational symmetry가 있는 object에서는 texture가 사실상 object orientation을 잘못 회전시키는 failure가 생길 수 있다. 이는 texture와 pose를 더 강하게 joint modeling하거나, pose-aware texture generation을 넣어야 할 지점이다.

추가로, SA-3DAO는 valuable benchmark지만 1K artist-created untextured objects 규모이므로, long-tail category와 manipulation-critical fine geometry에 대한 완전한 검증으로 보기는 어렵다. 또한 논문은 human preference를 강하게 사용하지만, robotics에서 중요한 physical validity, material/contact property, metric scale reliability, sensor noise robustness는 별도 평가가 필요하다.

### 10. 결론

SAM 3D의 가장 큰 contribution은 architecture 단독이 아니라 data engine과 staged training recipe다. 논문은 synthetic object render로 시작해 semi-synthetic render-paste로 occlusion/layout capability를 만들고, MITL/artist annotation과 DPO로 real-world behavior를 align하는 과정을 3D reconstruction에 성공적으로 이식한다.

기술적으로는 single image와 mask에서 shape, texture, layout을 동시에 생성한다는 점, 그리고 scene context를 recognition cue로 활용한다는 점이 중요하다. robotics 관점에서는 open-world object pose/shape proposal generator로 유용하지만, physical consistency가 보장되는 state estimator는 아니다. 따라서 실제 적용에서는 SAM 3D output을 RGB-D tracking, physics-aware optimization, collision checking, grasp feasibility evaluation과 결합하는 방식이 적절하다.

## 추가 질문과 답변

### 2026-05-22 19:56 - Object representation과 latent의 출처

**질문**

SAM 3D에서 사용한 object representation이나 latent는 어떻게 구성되는가? 이는 완전히 독자적인 설계인가, 아니면 특정 연구로부터 영감을 받았는가?

**답변**

SAM 3D의 object representation은 크게 두 단계로 나뉜다. 첫 번째 Geometry model은 coarse shape와 layout을 함께 생성한다. 논문에서 coarse shape는 $O \in \mathbb{R}^{64^3}$인 voxel latent로 표현되며, 이와 함께 rotation $R \in \mathbb{R}^{6}$, translation $t \in \mathbb{R}^{3}$, scale $s \in \mathbb{R}^{3}$를 직접 생성한다. Appendix C.1에 따르면 shape는 더 coarse한 $16^3 \times 8$ latent representation에서 denoising되어 $64^3$ voxel 형태로 다뤄지고, shape는 4096개 token, $R,t,s$는 각각 1개 token으로 Mixture-of-Transformers에 입력된다. 즉 SAM 3D의 첫 representation은 "3D object shape latent + explicit camera-relative layout parameter"의 결합이다.

두 번째 Texture & Refinement model은 Geometry model이 예측한 coarse shape $O$에서 active voxel을 추출한 뒤, sparse latent flow transformer로 geometric detail과 texture를 refine한다. 이 단계의 latent는 SLAT, 즉 structured 3D latent 계열이며, 최종 latent는 VAE decoder를 통해 mesh decoder $D_m$ 또는 3D Gaussian splat decoder $D_g$로 decode될 수 있다. 두 decoder는 같은 VAE encoder와 structured latent space를 공유한다.

따라서 이 설계는 완전히 독자적인 representation이라기보다는 Xiang et al. (2025), 즉 TRELLIS의 "Structured 3D Latents for Scalable and Versatile 3D Generation"을 강하게 기반으로 한다. 본문 Section 2.2가 명시적으로 "recent SOTA two-stage latent flow matching architectures (Xiang et al., 2025)" 위에 구축했다고 설명하고, Appendix C.1도 shape latent가 Xiang et al. (2025)를 따른다고 쓴다. Texture & Refinement 쪽 sparse latent flow transformer와 SLAT feature objective, mesh/Gaussian decoder 공유 latent space 역시 Xiang et al. (2025)에 기반한다.

SAM 3D의 독자적인 부분은 representation 자체를 처음 발명했다기보다는, 그 representation을 real-world object reconstruction에 맞게 확장한 쪽에 가깝다. 구체적으로는 isolated object reconstruction이 아니라 full image context와 object mask를 함께 condition하고, layout $(R,t,s)$를 shape와 함께 생성하며, MoT 구조로 shape token과 layout token 사이의 정보 공유를 설계한다. 또한 기존 SLAT VAE의 back-projection이 occluded voxel까지 feature를 넣어 sharpness를 낮춘다고 보고, visible voxel에만 depth-aware back-projection을 수행하는 Depth-VAE 변형을 추가한다. 요약하면 latent backbone은 TRELLIS/Xiang et al. 2025 계열이고, SAM 3D의 novelty는 여기에 real-world visual grounding, layout prediction, pointmap conditioning, Depth-VAE 수정, MITL/artist data engine과 post-training alignment를 결합한 데 있다.

### 2026-05-22 19:59 - Pictorial cue 논의

**질문**

pictorial cue 논의에 대해 설명해.

**답변**

SAM 3D에서 pictorial cue 논의는 "단일 이미지에서 어떻게 3D를 알 수 있는가?"라는 오래된 지각 심리학/컴퓨터 비전 문제를 모델 설계의 정당화로 가져오는 부분이다. 전통적인 3D vision은 multi-view geometry, stereo, SfM처럼 여러 시점의 대응점과 parallax를 주된 3D signal로 보았다. 반면 인간은 한 장의 그림이나 사진만 보고도 깊이, 표면 방향, 물체의 완전한 형태를 상당히 잘 추론한다. 이때 단일 이미지 안에 들어 있는 3D 단서들을 psychology textbook에서는 pictorial cues라고 부른다.

논문이 말하는 pictorial cue에는 shading, texture pattern, silhouette, occlusion, perspective 같은 low/mid-level visual cue뿐 아니라 recognition cue도 포함된다. 특히 저자들이 강조하는 것은 familiar object cue다. 예를 들어 이미지에서 다리 하나가 가려진 의자를 보면, 실제 pixel에는 보이지 않아도 의자라는 recognition이 작동하면서 대략적인 3D structure, symmetry, missing part, pose를 추론한다. 논문은 이를 "recognition enables 3D reconstruction"이라는 문장으로 요약한다.

이 관점은 SAM 3D의 architecture와 training에 직접 연결된다. 모델은 object crop만 보는 것이 아니라 full image도 함께 encode한다. crop은 local detail과 mask-following에 유리하지만, full image는 object category, scene context, support relation, occlusion pattern 같은 recognition cue를 준다. 즉 SAM 3D는 3D reconstruction을 pure geometry inversion으로만 보지 않고, visual recognition prior를 활용한 conditional generation 문제로 본다.

중요한 함의는 full 3D reconstruction이 관측된 visible surface의 단순 복원이 아니라는 점이다. 단일 이미지는 본질적으로 lossy projection이므로 backside, occluded part, true metric shape는 관측만으로 결정되지 않는다. 따라서 SAM 3D가 출력하는 것은 확정적 정답이라기보다 image와 mask, context, learned object prior에 조건화된 plausible 3D sample이다. 논문이 $p(S,T,R,t,s \mid I,M)$ 같은 conditional distribution을 설정하는 이유도 여기에 있다.

Robotics 관점에서는 이 논의가 양날의 칼이다. familiar object cue는 occlusion이 심한 real-world scene에서 useful prior를 제공해 manipulation candidate, pose proposal, simulation asset bootstrapping에 도움이 된다. 하지만 recognition prior는 hallucination도 만든다. 보이지 않는 뒷면이나 접촉 상태, 내부 구조, 물리적 안정성은 모델이 "그럴듯하게" 채우는 것이지 센서로 확인한 사실이 아니다. 따라서 robot deployment에서는 SAM 3D의 pictorial-cue 기반 reconstruction을 final geometry truth가 아니라 strong semantic-geometric prior로 다루고, depth, tactile sensing, multi-view verification, physics/collision checking으로 보정하는 편이 안전하다.

### 2026-05-22 20:02 - Semantic 정보와 object category 출력 여부

**질문**

그러면 SAM 3D는 생성한 object에 대한 semantic 정보도 포함하나? 즉, 물체의 카테고리를 맞출 수 있나?

**답변**

논문 기준으로는 SAM 3D가 semantic information을 "사용"한다고 말할 수는 있지만, 생성 결과에 explicit semantic label을 "출력"한다고 보기는 어렵다. SAM 3D의 공식 output은 shape $S$, texture $T$, rotation $R$, translation $t$, scale $s$이고, Geometry model도 $p(O,R,t,s \mid I,M)$를, Texture & Refinement model도 $p(S,T \mid I,M,O)$를 모델링한다. 여기에는 object category token이나 class label prediction head가 포함되어 있다고 설명되지 않는다.

다만 semantic recognition은 pipeline 안에서 매우 중요하다. 입력 encoding에서 full image context를 쓰는 이유가 cropped view에 없는 global scene context와 recognition cue를 얻기 위해서이고, 데이터 엔진도 VLM 기반 object recognition으로 object-level annotation을 만들고, LVIS 기반 3D-oriented taxonomy로 object distribution을 관리한다. Appendix A.1에서는 object category label을 보존하고 데이터 엔진을 통과하는 category distribution을 모니터링한다고 설명한다. 즉 category는 training data sourcing, balancing, annotation management에는 존재한다.

따라서 SAM 3D가 물체의 카테고리를 "내부적으로 맞추는 듯한" representation을 갖고 있을 가능성은 높다. 의자처럼 생긴 geometry와 texture를 만들려면 DINOv2/full-image context와 learned prior 안에 category-level semantics가 반영되어야 하기 때문이다. 하지만 이것은 implicit semantic representation이지, 논문이 평가하거나 보장하는 explicit classification output은 아니다.

실제로 category를 얻고 싶다면 두 가지 접근이 더 자연스럽다. 첫째, SAM 3D 앞단의 detector, VLM, open-vocabulary segmentation/referring model에서 category/description을 가져온다. 둘째, SAM 3D가 생성한 mesh/rendering을 다시 CLIP/VLM/3D classifier에 넣어 category를 추론한다. 후자는 가능하지만 SAM 3D 자체의 주된 task가 아니므로 category accuracy가 논문에서 검증된 것은 아니다.

Robotics 관점에서는 이 차이가 중요하다. SAM 3D output이 "cup-like geometry"를 만들었다고 해서 그것이 symbolic scene graph의 `cup` label을 신뢰도 있게 제공한다는 뜻은 아니다. manipulation pipeline에서는 SAM 3D를 geometry/layout prior로 쓰고, semantic label은 별도의 perception module 또는 VLM grounding 결과와 fuse하는 구성이 더 안전하다.
