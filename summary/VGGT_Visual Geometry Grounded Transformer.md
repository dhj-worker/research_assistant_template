# VGGT: Visual Geometry Grounded Transformer

## 메타데이터

- PDF 파일: `VGGT_Visual Geometry Grounded Transformer.pdf`
- 논문 제목: VGGT: Visual Geometry Grounded Transformer
- 저자: Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, David Novotny
- 소속: Visual Geometry Group, University of Oxford; Meta AI
- venue/arXiv: arXiv:2503.11651v1 [cs.CV]
- 연도: 2025
- DOI/URL: https://github.com/facebookresearch/vggt
- 작업 일시: 2026-05-22

## Abstract

We present VGGT, a feed-forward neural network that directly infers all key 3D attributes of a scene, including camera parameters, point maps, depth maps, and 3D point tracks, from one, a few, or hundreds of its views.

**우리는 하나, 몇 개, 또는 수백 개의 view로부터 camera parameter, point map, depth map, 3D point track을 포함한 scene의 핵심 3D attribute를 직접 추론하는 feed-forward neural network인 VGGT를 제시한다.**

This approach is a step forward in 3D computer vision, where models have typically been constrained to and specialized for single tasks.

**이 접근은 기존 model들이 대체로 단일 task에 제약되고 특화되어 있던 3D computer vision에서 한 걸음 나아간 것이다.**

It is also simple and efficient, reconstructing images in under one second, and still outperforming alternatives that require post-processing with visual geometry optimization techniques.

**또한 이 방법은 단순하고 효율적이어서 1초 미만에 image를 reconstruction하면서도, visual geometry optimization 기반 post-processing을 요구하는 대안들보다 더 좋은 성능을 낸다.**

The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking.

**이 network는 camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, 3D point tracking을 포함한 여러 3D task에서 state-of-the-art 결과를 달성한다.**

We also show that using pretrained VGGT as a feature backbone significantly enhances downstream tasks, such as non-rigid point tracking and feed-forward novel view synthesis.

**또한 pretrained VGGT를 feature backbone으로 사용하면 non-rigid point tracking과 feed-forward novel view synthesis 같은 downstream task가 크게 개선됨을 보인다.**

Code and models are publicly available at https://github.com/facebookresearch/vggt.

**Code와 model은 https://github.com/facebookresearch/vggt 에 공개되어 있다.**

## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 다시 확인했다.

1. Introduction
2. Related Work
   1. Structure from Motion
   2. Multi-view Stereo
   3. Tracking-Any-Point
3. Method
   1. Problem definition and notation
   2. Feature Backbone
   3. Prediction heads
   4. Training
4. Experiments
   1. Camera Pose Estimation
   2. Multi-view Depth Estimation
   3. Point Map Estimation
   4. Image Matching
   5. Ablation Studies
   6. Finetuning for Downstream Tasks
5. Discussions
6. Conclusions
7. Appendix
   1. Formal Definitions
   2. Implementation Details
   3. Additional Experiments
   4. Qualitative Examples
   5. Related Work

## 요약

### 1. 전체 구조

VGGT는 3D reconstruction을 "각 task별 specialized model과 geometry optimization을 조합하는 문제"가 아니라, "큰 transformer가 multi-view image set에서 scene-level 3D attribute를 한 번에 예측하는 문제"로 재정의한다. 입력은 같은 scene을 보는 $N$장의 RGB image이고, 출력은 각 frame의 camera parameter, depth map, world-coordinate point map, tracking feature이다.

논문의 핵심 함수는 다음처럼 요약된다.

$$
f((I_i)_{i=1}^{N}) = (g_i, D_i, P_i, T_i)_{i=1}^{N}
$$

여기서 $g_i$는 camera intrinsics/extrinsics, $D_i$는 depth map, $P_i$는 첫 번째 camera 좌표계에 놓인 viewpoint-invariant point map, $T_i$는 point tracking에 쓰이는 dense feature grid이다. 중요한 점은 VGGT가 이들을 별도 pipeline으로 순차 추정하지 않고, 하나의 shared transformer backbone과 여러 prediction head로 동시에 예측한다는 것이다.

논문은 DUSt3R/MASt3R 계열의 "pairwise point map prediction + global alignment" 흐름에서 더 나아간다. VGGT는 2-view pair만 처리하는 대신 하나, 몇 개, 수십 개, 수백 개 image를 직접 입력으로 받아 global scene reasoning을 한다. 결과적으로 SfM, MVS, dense point cloud, image matching, point tracking을 하나의 feed-forward model family 안에 묶는다.

### 2. Section 간 연결

Introduction은 classical SfM/MVS가 feature matching, triangulation, bundle adjustment 같은 iterative geometry pipeline에 의존하고, DUSt3R/MASt3R도 pairwise prediction 뒤 global alignment가 필요하다는 문제를 제기한다. Related Work는 SfM, MVS, tracking-any-point를 각각 정리하면서 VGGT가 이 세 task를 모두 포괄하려는 위치에 있음을 만든다.

Method는 먼저 출력 공간을 정의한다. Camera는 quaternion, translation, field-of-view로 표현하고, point map은 첫 번째 camera coordinate frame 기준으로 정의한다. 이어서 DINOv2 patch token과 alternating frame-wise/global self-attention으로 backbone을 만들고, camera token, DPT dense head, CoTracker2-style tracking head를 붙인다. Training section은 multi-task supervision, coordinate normalization, 대규모 dataset mixture, 1.2B parameter 학습 설정을 설명한다.

Experiments는 논문의 주장을 단계적으로 검증한다. Camera pose, multi-view depth, point map, two-view matching에서 기존 specialist 또는 optimization-heavy method를 넘는지 확인하고, ablation으로 alternating-attention과 multi-task learning의 기여를 분리한다. 마지막으로 downstream finetuning에서는 VGGT feature가 novel view synthesis와 dynamic tracking에도 유용함을 보인다. Discussion은 fisheye/panorama, extreme rotation, large non-rigid motion, memory cost 같은 실제 deployment상의 한계를 정리한다.

### 3. 핵심 주장과 근거

첫째, VGGT는 visual geometry task들을 하나의 feed-forward transformer로 통합할 수 있다고 주장한다. 이 주장의 근거는 출력 범위가 넓다는 점에 있다. VGGT는 camera pose만, depth만, point cloud만 예측하는 것이 아니라 이들을 모두 동시에 예측한다. 논문은 서로 닫힌 형식으로 연결되는 over-complete output을 함께 supervision하면 성능이 좋아진다고 보고한다. 예를 들어 point map은 camera와 depth에서 역투영할 수 있지만, point map head도 같이 학습하면 shared feature가 더 좋은 geometry representation을 배운다는 것이다.

둘째, minimal 3D inductive bias와 대규모 3D-annotated data가 결합되면 explicit geometry solver 없이도 강한 reconstruction 성능을 낼 수 있다고 주장한다. Architecture는 DINOv2 tokenization, transformer self-attention, DPT head에 가깝고, cost volume, epipolar matching layer, differentiable BA를 기본 구성에 넣지 않는다. 3D prior는 architecture보다 training objective와 data에서 온다.

셋째, alternating-attention이 multi-view set 처리에 적합하다고 주장한다. 각 block은 frame-wise self-attention과 global self-attention을 번갈아 수행한다. Frame-wise attention은 각 image 내부의 token activation과 local structure를 안정화하고, global attention은 frame 간 correspondence와 scene consistency를 통합한다. Table 5에서 ETH3D point map overall score는 cross-attention $1.061$, global self-attention only $0.827$, alternating-attention $0.709$로 보고되어, 제안 구조가 가장 좋다.

넷째, feed-forward mode 자체가 이미 강하고, BA는 선택적 refinement로 남는다. VGGT는 Re10K/CO3Dv2 camera pose에서 feed-forward만으로 기존 method를 앞서며, BA를 붙이면 더 좋아진다. 이는 VGGT가 visual geometry optimization을 완전히 부정한다기보다, optimization을 필수 pipeline에서 optional refinement로 낮춘다는 의미에 가깝다.

### 4. Robotics 관점의 novelty와 relevance

Robotics 관점에서 VGGT의 가장 큰 매력은 빠른 multi-view metric-ish scene geometry initialization이다. Robot perception pipeline에서 camera pose, depth, dense point cloud, correspondence는 SLAM, manipulation, reconstruction, view planning, digital twin update의 기초 primitive이다. VGGT는 이 primitive들을 개별 module로 연결하지 않고 한 번의 forward pass로 제공하므로, perception bootstrapping이나 online reconstruction 초기값 생성에 유용할 수 있다.

특히 다음 용도가 자연스럽다.

1. Unknown object/scene의 fast multi-view geometry prior
2. Robot-collected image burst에서 camera pose와 depth를 빠르게 초기화
3. Dense point cloud를 downstream Gaussian splatting, mesh reconstruction, occupancy mapping에 연결
4. Learned correspondence feature를 tracking, visual servoing, manipulation keypoint tracking에 활용
5. BA, SLAM, NeRF/3DGS optimization의 initialization으로 사용

하지만 robot deployment에 바로 넣기에는 주의가 필요하다. VGGT는 첫 번째 camera 기준 coordinate와 scale normalization을 사용하므로, absolute metric scale은 sensor calibration, depth sensor, known object size, robot kinematics 등 외부 정보와 맞춰야 한다. 또한 fisheye/panorama 미지원, extreme rotation 성능 저하, 큰 non-rigid deformation failure가 명시되어 있어, mobile robot wide-FOV camera나 wrist camera의 급격한 motion에서는 별도 finetuning/검증이 필요하다.

논문은 real-time application에 적합하다고 말하지만, 수백 frame 입력 시 memory cost가 크다. Table 9에서 336 x 518 image 기준 100 frame은 3.12초와 21.15GB, 200 frame은 8.75초와 40.63GB를 사용한다. Robot onboard GPU에서 수백 frame을 한 번에 처리하기보다는 keyframe selection, chunked inference, frame-by-frame DPT head 처리, BA/SLAM과의 hybridization이 현실적이다.

### 5. 기존 방법과 비교

| 구분 | 기존 방법 | 본 논문 | 의미 |
|---|---|---|---|
| Classical SfM/MVS | Matching, triangulation, BA, dense stereo를 단계별로 수행 | Camera, depth, point map, tracking feature를 feed-forward로 동시 예측 | Pipeline complexity와 test-time optimization 의존도를 줄임 |
| DUSt3R/MASt3R | Pairwise point map prediction 뒤 global alignment 필요 | Multi-view set 전체를 한 번에 transformer로 처리 | 수십-수백 view에서 pair fusion 병목을 완화 |
| VGGSfM | Deep SfM이지만 differentiable BA와 SfM pipeline 구조가 강함 | BA 없이도 camera pose를 직접 예측하고, BA는 optional refinement | Neural-first geometry estimation 방향 |
| MVSNet/GeoMVSNet류 | Known camera로 cost volume을 구성 | Unknown camera에서도 depth/point를 예측 | Pose-free MVS 성격을 가짐 |
| Specialized tracker | Dynamic point tracking 전용 architecture | Static multi-view feature를 CoTracker에 이식해 dynamic tracking 개선 | VGGT feature가 correspondence backbone으로도 유효 |
| Novel view synthesis model | 대개 input camera pose를 요구 | VGGT finetuning은 input camera parameter 없이 target view synthesis 가능 | Pose-free representation의 downstream 확장성 |

Camera pose estimation에서 VGGT의 결과는 특히 강하다. RealEstate10K/CO3Dv2 10-frame setting에서 VGGT feed-forward는 AUC@30 $85.3/88.2$를 기록하고, BA를 추가하면 $93.5/91.8$로 상승한다. 비교 대상인 MASt3R은 $67.7/76.7$, VGGSfM v2는 $78.9/83.4$, Fast3R은 $72.7/82.5$이다. 논문은 feed-forward runtime을 0.2초, BA 포함 runtime을 1.8초로 보고한다.

Dense MVS에서는 DTU dataset에서 unknown camera setting의 DUSt3R overall $1.741$ 대비 VGGT는 $0.382$를 기록한다. 이는 known ground-truth camera를 사용하는 MASt3R $0.374$, GeoMVSNet $0.295$와 비교 가능한 수준이다. 즉 pose-free feed-forward model이 camera-known MVS method에 근접한 dense geometry를 낸다는 점이 핵심 메시지다.

ETH3D point map estimation에서는 DUSt3R $1.005$, MASt3R $0.826$ 대비 VGGT point head가 $0.709$, depth+camera unprojection이 $0.677$을 기록한다. 흥미로운 점은 직접 point map head보다 camera+depth로 3D point를 구성하는 쪽이 더 정확하다는 것이다. 이는 output을 함께 학습하더라도 inference에서는 task decomposition이 더 안정적일 수 있음을 보여준다.

Image matching에서는 ScanNet-1500 two-view pose AUC가 SuperGlue $16.2/33.8/51.8$, LoFTR $22.1/40.8/57.6$, DKM $29.4/50.7/68.3$, Roma $31.8/53.4/70.9$인데, VGGT는 $33.9/55.2/73.4$로 가장 높다. VGGT tracking head가 two-view matching 전용으로 설계되지 않았다는 점을 고려하면, learned geometry feature의 범용성을 보여주는 실험이다.

### 6. Implementation idea

VGGT의 구현은 다음 pipeline으로 볼 수 있다.

1. Image tokenization
   - 각 RGB image $I_i$를 DINOv2로 patchify해 image token $t_i^I$를 얻는다.
   - 각 frame에 camera token $t_i^g$와 register token을 붙인다.
   - 첫 번째 frame에는 별도 learnable token을 사용해 reference frame임을 알려준다.

2. Alternating-attention transformer
   - 기본 설정은 24개 block이며, 각 block은 frame-wise self-attention과 global self-attention을 포함한다.
   - Frame-wise attention은 frame 내부 token만 attend하고, global attention은 모든 frame token을 함께 attend한다.
   - Cross-attention layer 없이 self-attention만 사용한다.

3. Camera head
   - Output camera token에 self-attention layer 4개와 linear layer를 적용한다.
   - Camera parameter는 $g=[q,t,f]$이며, $q \in \mathbb{R}^4$, $t \in \mathbb{R}^3$, $f \in \mathbb{R}^2$이다.
   - 첫 번째 camera extrinsic은 identity로 고정한다.

4. Dense prediction head
   - Output image token을 DPT layer로 dense feature map $F_i$로 upsample한다.
   - $3 \times 3$ convolution으로 depth map $D_i$, point map $P_i$, tracking feature $T_i$를 예측한다.
   - Depth와 point map에는 aleatoric uncertainty map도 함께 예측해 loss weighting에 사용한다.

5. Tracking head
   - CoTracker2 architecture를 사용한다.
   - Query point feature를 bilinear sample하고, 다른 frame의 dense tracking feature와 correlation map을 만든 뒤 self-attention으로 track을 예측한다.
   - VGGT의 tracking은 temporal order를 가정하지 않으므로 unordered image set에도 적용 가능하다.

6. Training
   - Camera, depth, point map, tracking loss를 multi-task로 학습한다.
   - 2-24 frame을 random scene에서 sample하고, batch 전체는 48 frame을 유지한다.
   - 518 pixel 최대 해상도, aspect ratio augmentation, color jitter, Gaussian blur, grayscale augmentation을 사용한다.
   - 1.2B parameter model을 64 A100 GPU에서 160K iteration, 약 9일 동안 학습한다.

### 7. Mathematical background

VGGT는 scale/reference-frame ambiguity를 normalization으로 고정한다. 모든 quantity를 첫 번째 camera coordinate frame에 표현하고, 3D point의 평균 Euclidean distance로 translation, point map, depth를 normalize한다. 이 설정은 monocular/multi-view image만으로는 global scale과 rigid transform이 관측 불가능하다는 visual geometry의 기본 ambiguity를 network training target에서 제거하기 위한 것이다.

Camera parameter는 다음처럼 구성된다.

$$
g = [q, t, f]
$$

여기서 $q$는 rotation quaternion, $t$는 translation, $f$는 field of view이다. Principal point는 image center로 가정한다.

Point map $P_i(y)$는 pixel $y$가 대응하는 3D scene point를 첫 번째 camera coordinate frame에서 표현한 것이다. Depth $D_i(y)$는 $i$번째 camera에서 본 해당 pixel의 depth이다. 이론적으로 camera와 depth가 있으면 point map을 구성할 수 있다. 논문이 중요하게 보는 부분은 이러한 redundancy를 제거하지 않고 over-complete하게 학습한다는 점이다.

Training objective는 다음 multi-task loss이다.

$$
L = L_{\mathrm{camera}} + L_{\mathrm{depth}} + L_{\mathrm{pmap}} + L_{\mathrm{track}}
$$

본문 설명상 tracking loss는 실제 학습에서 $\lambda=0.05$로 down-weight된다. Camera loss는 predicted camera와 ground-truth camera 사이의 Huber loss이다. Depth와 point map loss는 DUSt3R 계열의 aleatoric uncertainty loss를 따르며, depth에는 gradient-based term도 추가한다. Tracking loss는 query point의 target-frame correspondence error와 visibility binary cross-entropy를 포함한다.

논문이 보여주는 흥미로운 구조적 사실은 point map이 직접 output head로 존재하지만, inference에서 더 좋은 point cloud는 다음 방식으로 얻어진다는 점이다.

$$
\hat{P}_i(y) = \mathrm{unproject}(y, \hat{D}_i(y), \hat{g}_i)
$$

Table 3에서 depth+camera 기반 point cloud가 point head 직접 출력보다 좋다. 이는 model이 point map을 같이 학습하면서 representation은 좋아졌지만, 최종 geometry consistency는 camera-depth decomposition을 거치는 편이 더 강할 수 있음을 시사한다.

### 8. Experiments

학습 데이터는 매우 다양하다. Co3Dv2, BlendMVS, DL3DV, MegaDepth, Kubric, WildRGB, ScanNet, HyperSim, Mapillary, Habitat, Replica, MVS-Synth, PointOdyssey, Virtual KITTI, Aria Synthetic Environments, Aria Digital Twin, artist-created synthetic asset dataset을 사용한다. Annotation source는 sensor capture, synthetic engine, SfM 등으로 섞여 있다. 논문은 전체 data mixture의 규모와 다양성이 MASt3R와 broadly comparable하다고 설명한다.

Camera pose evaluation은 CO3Dv2와 RealEstate10K에서 10 random frame을 뽑아 AUC@30을 측정한다. RRA/RTA의 threshold curve 아래 면적을 사용하며, RealEstate10K는 train에 포함되지 않은 unseen dataset이다. VGGT feed-forward가 Re10K $85.3$, CO3Dv2 $88.2$를 기록해, BA를 쓰는 VGGSfM v2 $78.9/83.4$보다 높다. VGGT+BA는 $93.5/91.8$로 더 높아진다.

Multi-view depth estimation은 DTU에서 Accuracy, Completeness, Overall Chamfer score를 측정한다. VGGT는 unknown camera setting에서 Acc. $0.389$, Comp. $0.374$, Overall $0.382$를 기록한다. DUSt3R의 Overall $1.741$보다 훨씬 좋고, known camera를 사용하는 MASt3R $0.374$와 거의 같은 수준이다. 다만 GeoMVSNet $0.295$처럼 camera-known MVS 전용 method에는 여전히 차이가 있다.

Point map estimation은 ETH3D에서 10 frame을 random sample하고, predicted point cloud를 Umeyama alignment로 ground truth에 맞춘 뒤 Chamfer를 계산한다. VGGT depth+camera 방식은 Acc. $0.873$, Comp. $0.482$, Overall $0.677$을 기록한다. MASt3R의 Overall $0.826$, DUSt3R의 $1.005$보다 좋으며, runtime도 0.2초로 훨씬 빠르다.

Image matching은 ScanNet-1500에서 relative pose AUC@5/10/20을 측정한다. VGGT는 $33.9/55.2/73.4$로 Roma $31.8/53.4/70.9$를 넘는다. 여기서 keypoint detection은 ALIKED를 사용하고, VGGT tracking branch가 correspondence를 찾는다.

Ablation은 두 가지가 중요하다.

1. Backbone ablation
   - Cross-attention: ETH3D Overall $1.061$
   - Global self-attention only: $0.827$
   - Alternating-attention: $0.709$

2. Multi-task learning ablation
   - Full model이 ETH3D Overall $0.709$로 가장 좋다.
   - Camera loss, depth loss, tracking loss를 제거하면 point map accuracy가 떨어진다.
   - 특히 camera estimation supervision이 point map 품질에 큰 기여를 한다.

Downstream finetuning도 인상적이다. Novel view synthesis에서는 VGGT를 target-view RGB regression으로 finetune해 GSO dataset에서 PSNR $30.41$, SSIM $0.949$, LPIPS $0.033$을 얻는다. LVSM의 $31.71/0.957/0.027$보다는 낮지만, VGGT는 input camera parameter를 받지 않고 더 작은 training set을 사용한다. Dynamic point tracking에서는 CoTracker backbone을 VGGT pretrained feature로 바꿔 TAP-Vid RGB-S의 $\mathrm{avvisg}$를 $78.9$에서 $84.0$으로 개선한다.

### 9. Limitations and future work

논문이 명시한 limitation은 다음과 같다.

1. 현재 model은 fisheye 또는 panoramic image를 지원하지 않는다.
2. Extreme input rotation 조건에서 reconstruction 성능이 떨어진다.
3. Minor non-rigid motion은 어느 정도 처리하지만, substantial non-rigid deformation에서는 실패한다.
4. 많은 frame을 처리할 때 global self-attention의 memory cost가 커진다.

추가로 해석상 주의할 점도 있다.

- Absolute metric scale은 image-only setup에서 본질적으로 모호하다. Robotics에서는 robot calibration, depth, known object scale과 결합해야 한다.
- Principal point를 image center로 가정하므로, 실제 camera calibration이 크게 어긋나는 경우 pose/depth 품질이 흔들릴 수 있다.
- Feed-forward prediction은 빠르지만, long-term temporal consistency나 loop closure를 보장하는 SLAM system은 아니다.
- BA를 붙이면 더 좋아진다는 결과는, pure neural prediction만으로 최종 geometric consistency가 완전히 해결된 것은 아님을 보여준다.
- Training data가 대규모 public/synthetic 3D annotated dataset에 의존하므로, robotics 현장의 domain shift, motion blur, rolling shutter, reflective/transparent object, low-texture industrial scene은 별도 검증이 필요하다.

Future work 관점에서는 fisheye/wide-FOV camera finetuning, robot ego-motion prior 결합, online keyframe memory, metric scale calibration, differentiable BA의 efficient training integration, dynamic scene decomposition이 자연스럽다. 논문도 differentiable BA를 preliminary experiment로 검토했지만 training step이 약 4배 느려져 본 작업에는 포함하지 않았다고 설명한다.

### 10. 결론

VGGT는 visual geometry의 고전적 pipeline을 "optimization-first"에서 "large feed-forward model first"로 이동시키는 논문이다. Camera pose, depth, point map, track을 하나의 transformer가 동시에 예측하고, BA나 global alignment 없이도 여러 3D task에서 강한 성능을 낸다. DUSt3R/MASt3R가 열어 둔 point-map 기반 neural geometry 방향을 multi-view set transformer와 multi-task supervision으로 확장한 작업으로 볼 수 있다.

Robotics 연구자에게는 특히 빠른 geometry/correspondence prior로 읽는 것이 좋다. VGGT는 robot-ready 3D world model이라기보다는, SLAM, reconstruction, manipulation perception, view synthesis, synthetic scene update의 초기값과 feature backbone으로 쓸 수 있는 강한 visual geometry foundation model에 가깝다. 실제 robot deployment에는 calibration, metric scale, temporal consistency, dynamic object handling, memory budget 검증이 추가로 필요하다.

## 추가 질문과 답변
