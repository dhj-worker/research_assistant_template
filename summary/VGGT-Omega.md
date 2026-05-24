# VGGT-$\Omega$

## 메타데이터

- PDF 파일: `VGGT-Omega.pdf`
- 논문 제목: VGGT-$\Omega$
- 저자: Jianyuan Wang, Minghao Chen, Shangzhan Zhang, Nikita Karaev, Johannes Schönberger, Patrick Labatut, Piotr Bojanowski, David Novotny, Andrea Vedaldi, Christian Rupprecht
- 소속: Visual Geometry Group, University of Oxford; Meta AI
- venue/arXiv: arXiv:2605.15195v1 [cs.CV]
- 연도: 2026
- DOI/URL: https://arxiv.org/abs/2605.15195, http://vggt-omega.github.io/
- 작업 일시: 2026-05-24 09:08

## Abstract

Recent feed-forward reconstruction models, such as VGGT, have proven competitive with traditional optimization-based reconstructors while also providing geometry-aware features useful for other tasks.

**VGGT 같은 최근 feed-forward reconstruction model은 전통적인 optimization-based reconstructor와 경쟁 가능한 성능을 보이면서도, 다른 task에 유용한 geometry-aware feature를 제공한다는 점을 입증했다.**

Here, we show that the quality of these models scales predictably with model and data size.

**이 논문은 이러한 model의 품질이 model size와 data size에 따라 예측 가능한 방식으로 scaling됨을 보인다.**

We do so by introducing VGGT-$\Omega$, which substantially improves reconstruction accuracy, efficiency, and capabilities for both static and dynamic scenes.

**이를 위해 static scene과 dynamic scene 모두에서 reconstruction accuracy, efficiency, capability를 크게 개선한 VGGT-$\Omega$를 제안한다.**

To enable training this model at an unprecedented scale, we introduce architectural changes that improve training efficiency, a high-quality data annotation pipeline that supports dynamic scenes, and a self-supervised learning protocol.

**이 model을 전례 없는 scale로 학습하기 위해, training efficiency를 높이는 architecture 변경, dynamic scene을 지원하는 고품질 data annotation pipeline, 그리고 self-supervised learning protocol을 도입한다.**

We simplify VGGT's architecture by using a single dense prediction head with multi-task supervision and removing the expensive high-resolution convolutional layers.

**VGGT의 architecture를 단순화하여 multi-task supervision을 단일 dense prediction head에 적용하고, 비용이 큰 high-resolution convolutional layer를 제거한다.**

We also use registers to aggregate scene information into a compact representation and introduce register attention, which restricts inter-frame information exchange to these registers, in part replacing global attention.

**또한 register를 사용해 scene information을 compact representation으로 집약하고, frame 간 information exchange를 register로 제한하는 register attention을 도입해 global attention의 일부를 대체한다.**

In this way, during training, VGGT-$\Omega$ uses only about 30% of the GPU memory of its predecessor, allowing us to train with 15x more supervised data than prior work and to leverage vast amounts of unlabeled video data.

**이 방식으로 VGGT-$\Omega$는 training 중 predecessor GPU memory의 약 30%만 사용하며, 이전 연구보다 15배 많은 supervised data와 대규모 unlabeled video data를 활용할 수 있게 한다.**

VGGT-$\Omega$ achieves strong results for reconstruction of static and dynamic scenes across multiple benchmarks, for example, improving over the previous best camera estimation accuracy on Sintel by 77%.

**VGGT-$\Omega$는 여러 benchmark에서 static/dynamic scene reconstruction의 강한 결과를 달성하며, 예를 들어 Sintel의 camera estimation accuracy에서 기존 최고 성능을 77% 개선한다.**

We also show that the learned registers can improve vision-language-action models and support alignment with language, suggesting that reconstruction can be a powerful and scalable proxy task for spatial understanding.

**또한 learned register가 vision-language-action model을 개선하고 language alignment를 지원할 수 있음을 보여, reconstruction이 spatial understanding을 위한 강력하고 scalable한 proxy task가 될 수 있음을 시사한다.**

Project page: http://vggt-omega.github.io/

**Project page는 http://vggt-omega.github.io/ 이다.**

## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 다시 확인했다.

1. Introduction
2. Related work
   1. 3D Reconstruction
   2. Registers in Vision Transformers (ViTs)
3. Method
   1. A New Scalable Architecture
      1. Feature Extraction and Tokenization
      2. Register Attention
      3. Decoding
   2. Training Losses
   3. Dynamic Reconstruction
   4. Self-supervised Training
   5. Training Data
      1. Data Sources
      2. Data Annotation Pipeline
4. Experiments
   1. Implementation Details
   2. Benchmarking
   3. Ablation Studies
   4. Applications of Registers
5. Further Insights
6. Discussion
7. Conclusion
8. Supplementary Material
   1. Additional Details
   2. Common Data Issues
   3. Limitations

## 요약

### 1. 전체 구조

VGGT-$\Omega$는 VGGT 계열 feed-forward 3D reconstruction model의 scaling 논문이다. 기존 VGGT가 camera, depth, point map, tracking feature를 하나의 transformer로 예측해 "optimization-first 3D reconstruction"을 "feed-forward-first 3D reconstruction"으로 밀어붙였다면, VGGT-$\Omega$는 이 패러다임이 model size, data size, unlabeled video data, dynamic scene까지 확장되는지 실험한다.

핵심 입력과 출력은 다음과 같다.

$$
((g_1,D_1), \ldots, (g_N,D_N)) = f(I_1,\ldots,I_N)
$$

여기서 $I_i$는 입력 image, $D_i \in \mathbb{R}^{H \times W}$는 depth map, $g_i=(q_i,t_i,f_i) \in \mathbb{R}^{9}$는 quaternion rotation $q_i$, translation $t_i$, field-of-view $f_i$로 구성된 camera parameter이다. VGGT와 달리 VGGT-$\Omega$는 point map과 tracking feature를 직접 output head로 예측하지 않는다. 대신 point와 matching supervision을 training-only loss로 유지해 representation 학습에는 쓰되, inference output은 camera와 depth 중심으로 단순화한다.

논문의 세 가지 축은 명확하다.

1. Architecture scaling: register attention, 단일 dense head, 경량 upsampling head로 training memory를 VGGT 대비 약 30%로 줄인다.
2. Data scaling: public dataset과 internal Internet-style video annotation pipeline을 결합해 약 4M sequence를 만들고, VGGT보다 15배 많은 supervised data를 사용한다.
3. Self-supervised scaling: teacher-student protocol로 18M unlabeled video를 활용해 generalization을 개선한다.

결과적으로 이 논문은 단순한 "VGGT v2"라기보다, feed-forward reconstruction을 3D/4D spatial foundation model 후보로 scale up할 때 무엇이 병목이고 어떤 design이 유효한지 보여주는 engineering/scaling study에 가깝다.

### 2. Section 간 연결

Introduction은 VGGT 이후 feed-forward reconstruction model이 SfM/MVS optimization pipeline과 경쟁 가능해졌고, 그 feature가 VLA, VLM, video generation, perception task로 확장되고 있다는 배경에서 출발한다. 여기서 논문은 LLM/2D foundation model처럼 3D reconstruction model도 scaling law를 갖는지 묻는다.

Related work는 end-to-end SfM, DUSt3R/MASt3R, VGGT, dynamic 4D reconstruction, register token 연구를 묶는다. 핵심 위치는 "multi-view geometry를 explicit solver에 맡기는 방식"과 "learned feed-forward reconstruction" 사이이며, VGGT-$\Omega$는 후자를 더 큰 data/model regime으로 끌고 간다.

Method는 VGGT-$\Omega$의 architecture 변경을 설명한다. DINOv3 tokenization, camera token, per-frame scene token/register, alternating global/frame attention은 유지하되, 일부 global attention을 register attention으로 바꾼다. Dense prediction에서는 DPT high-resolution convolution block을 MLP + pixel shuffle 기반 head로 대체하고, point/tracking dense head를 제거한다. Training section은 camera/depth/point/matching loss, dynamic reconstruction representation, self-supervised teacher-student learning, annotation pipeline을 설명한다.

Experiments는 camera pose와 depth를 static/dynamic benchmark에서 검증하고, scaling curve, register attention, multi-task loss, self-supervision, annotation quality를 ablation한다. 이후 register application에서는 frozen scene token을 OpenVLA-OFT에 붙여 LIBERO 성능을 올리고, register-language contrastive alignment가 가능한지 보여준다.

Discussion과 Supplement는 이 논문에서 특히 중요하다. 논문은 feed-forward reconstruction이 optimization을 대체한다기보다, 빠르고 robust한 initialization과 geometry-aware representation을 제공한다고 말한다. 동시에 motion blur, 급격한 FOV 변화, distorted camera, noisy training labels, masked sensitive content 같은 한계를 명시한다.

### 3. 핵심 주장과 근거

첫째, feed-forward reconstruction은 model/data scaling에 따라 예측 가능하게 좋아진다. Figure 1에서 model size를 0.2B에서 10B로 키우면 평균 point error가 $0.107 \rightarrow 0.073 \rightarrow 0.057 \rightarrow 0.046$으로 감소한다. Data size도 2K에서 2M sequence로 늘리면 point error가 $0.275 \rightarrow 0.210 \rightarrow 0.160 \rightarrow 0.129 \rightarrow 0.073$으로 단조 감소한다. 논문은 이를 power-law-like scaling으로 해석한다.

둘째, register는 단순 auxiliary token이 아니라 scene-level information bottleneck이 될 수 있다. VGGT-$\Omega$는 frame마다 16개 register를 붙이고, 일부 global attention layer에서 image token 전체가 아니라 register끼리만 inter-frame attention을 수행한다. 이후 frame-wise attention에서 register가 각 frame image token과 상호작용해 global scene information을 다시 분배한다. 25% global attention을 register attention으로 대체해도 point error는 $0.071$에서 $0.073$으로 거의 유지되고, training backbone FLOPs와 memory를 각각 약 23%, 16% 줄인다.

셋째, redundant output head를 줄여도 multi-task supervision의 이점은 대부분 유지된다. 기존 VGGT는 depth, point map, tracking feature를 dense head로 직접 예측했지만, VGGT-$\Omega$는 depth head 하나와 camera head 하나만 유지한다. Point map은 predicted depth와 camera의 unprojection으로 얻고, matching은 last-layer token에 loss만 건다. Point/matching loss를 제거하면 point error가 $0.073$에서 $0.078$로 나빠지므로 supervision 자체는 중요하지만, 별도 dense head가 꼭 필요한 것은 아니라는 결론이다.

넷째, dynamic scene 처리는 explicit dynamic output보다 data-driven prior에 맡긴다. 논문은 dynamic point map, motion mask, ray map 같은 출력을 추가하지 않는다. 대신 camera와 depth만 예측하고, dynamic scene을 포함한 대규모 annotated/unlabeled video로 prior를 학습한다. 이는 stationary camera가 dancer를 보는 경우처럼 scene motion과 camera motion이 섞이기 쉬운 상황에서 output representation을 단순하게 유지하려는 선택이다.

다섯째, reconstruction objective는 spatial representation 학습의 proxy task가 될 수 있다. Frozen VGGT-$\Omega$ scene token을 OpenVLA-OFT에 추가하면 LIBERO 평균 success rate가 $97.1\%$에서 $98.5\%$로 오른다. Language alignment 실험에서는 register-derived embedding으로 100개 video-description retrieval에서 top-1 $76.8\%$, top-3 $97.0\%$를 얻는다. 이는 register가 geometry만이 아니라 scene-level semantic/spatial information도 담는다는 간접 증거다.

### 4. Robotics 관점의 novelty와 relevance

Robotics 관점에서 VGGT-$\Omega$의 가치는 빠른 camera/depth estimation 그 자체보다, "large-scale reconstruction-pretrained spatial encoder"라는 점에 있다. Robot manipulation, navigation, active reconstruction, SLAM, visual servoing, VLA policy는 모두 depth, camera pose, object/scene geometry, view correspondence, motion cue에 민감하다. VGGT-$\Omega$는 이 primitive들을 직접 또는 latent register 형태로 제공한다.

특히 다음 활용이 자연스럽다.

1. Robot-collected multi-view burst에서 빠른 pose/depth initialization
2. RGB-only setup에서 dense depth와 camera prior를 얻어 SLAM/BA/3DGS/NeRF optimization 초기값으로 사용
3. VLA policy 입력에 frozen scene token을 추가해 spatial awareness를 보강
4. Dynamic scene에서 explicit optical flow/motion segmentation 없이 motion-aware feature를 얻는 backbone으로 사용
5. 새로운 robot domain에 작은 learning-rate schedule로 finetuning해 reconstruction prior를 적응

다만 deployment에는 주의가 필요하다. 논문은 principal point를 image center로 가정하고, camera/depth를 first camera coordinate frame과 normalized scale에서 다룬다. Robot에서 metric scale, hand-eye calibration, rolling shutter, fisheye/wide-FOV camera, reflective/transparent object, thin structure, motion blur는 별도 검증이 필요하다. 또한 feed-forward reconstruction은 loop closure와 long-horizon map consistency를 보장하는 SLAM system이 아니다. 논문도 COLMAP/BA가 well-conditioned setting에서 여전히 매우 높은 camera precision을 낼 수 있고, feed-forward model은 strong initialization으로 함께 쓰일 수 있다고 명시한다.

### 5. 기존 방법과 비교

| 구분 | 기존 방법 | VGGT-$\Omega$ | 의미 |
|---|---|---|---|
| COLMAP/SfM/MVS | Feature matching, triangulation, BA, dense stereo를 단계적으로 수행 | Camera와 depth를 feed-forward로 직접 예측 | 속도와 robustness는 좋아지지만, 최종 high-precision calibration은 BA가 여전히 유용 |
| VGGT | Alternating attention, 여러 dense head, point/track direct prediction | Register attention, single dense head, training-only point/matching loss | Scaling 가능한 architecture로 정리 |
| DUSt3R/MASt3R | Pairwise prediction 후 multi-view optimization/alignment 필요 | Multi-view set을 직접 처리하고 dynamic data까지 확장 | Pairwise fusion 병목 완화 |
| MegaSaM | Dynamic optimization 기반으로 강한 dynamic reconstruction | Feed-forward로 Sintel AUC@3 $40.0$ vs MegaSaM $22.5$ | Dynamic benchmark strict threshold에서도 큰 개선 |
| DA3/PI3 | VGGT-style dynamic reconstruction 계열 | 10B scaling, register attention, larger supervised/self-supervised data | Static/dynamic camera/depth 모두에서 상위 성능 |
| VLA encoder | 보통 2D visual token이나 action-conditioned token 사용 | Frozen scene token을 OpenVLA-OFT에 추가 | Reconstruction-pretrained register가 robot policy에 유용함을 보임 |

Camera pose 결과는 논문의 가장 강한 수치 근거다. Ours-10B는 AUC@3/AUC@30 기준으로 7 Scenes $36.4/88.2$, NRGBD $92.5/99.1$, ETH3D $56.3/90.4$, DyCheck $43.7/90.9$, Sintel $40.0/79.1$, TUM-Dynamic $36.4/87.5$를 기록한다. 특히 Sintel에서는 MegaSaM의 $22.5/58.3$을 크게 앞선다.

Depth 결과도 static/dynamic 양쪽에서 강하다. Ours-10B는 $\delta_{1.25}$/AbsRel 기준으로 7 Scenes $96.3/0.050$, NRGBD $99.7/0.007$, ETH3D $99.8/0.009$, DyCheck $98.7/0.030$, Sintel $93.5/0.081$, TUM-Dynamic $98.3/0.035$를 기록한다. 논문이 강조하는 예시는 Sintel에서 DA3의 $86.1/0.118$ 대비 $93.5/0.081$로 개선된 부분이다.

속도/메모리 비교에서는 VGGT-$\Omega$와 corrected VGGT가 single A100 80GB에서 약 1250 frame까지 처리 가능하고, DA3-Giant는 약 750 frame 근처에서 memory limit에 도달한다. VGGT-$\Omega$는 DINOv3 patch size 16과 25% register attention 덕분에 VGGT보다 빠르며, 모든 global attention을 register attention으로 바꾸는 aggressive variant는 1000 frame runtime을 240.2초에서 11.7초로 줄이지만 정확도가 original VGGT 수준으로 떨어진다.

### 6. Implementation idea

VGGT-$\Omega$의 구현 흐름은 다음처럼 정리할 수 있다.

1. Tokenization
   - 각 image $I_i$를 DINOv3-initialized ViT로 patch token $z_i^F$로 변환한다.
   - 각 frame에 camera token $z_i^{cam}$과 16개 scene token/register $z_i^{scene}$를 붙인다.
   - Reference image인지 아닌지를 나타내는 learnable parameter는 유지하지만, frame identity/order embedding은 사용하지 않는다.

2. Alternating attention with register attention
   - 기본 block은 global attention 또는 register attention과 frame-wise attention을 포함한다.
   - Frame-wise attention은 각 image 내부 token에만 작동한다.
   - Global attention은 모든 frame token을 함께 attend한다.
   - Register attention은 모든 frame의 register token끼리만 attend하고, image token 간 inter-frame attention을 생략한다.
   - 기본 설정에서는 global attention layer의 25%를 register attention으로 대체한다.

3. Decoding
   - Camera head는 camera token과 register를 lightweight transformer에 넣고, 각 camera token에 MLP를 적용해 $g_i=(q_i,t_i,f_i)$를 예측한다.
   - Depth head는 DPT의 low-resolution convolutional layer 일부는 유지하되, high-resolution convolution block은 single MLP + pixel shuffle로 대체한다.
   - 출력 channel은 depth와 confidence다.

4. Training-only supervision
   - Point map은 output head로 직접 만들지 않고, predicted depth와 camera로 unprojection한 point에 point loss를 건다.
   - Matching loss는 last attention layer token에 대해 positive/negative patch pair contrastive supervision을 건다.
   - Dynamic region의 match는 Grounding DINO로 movable object를 찾아 제외한다.

5. Data pipeline
   - Public dataset과 internal Internet-style video를 결합한다.
   - VLM pre-filter가 reconstruction에 부적합한 video를 제거하고 scene dynamics metadata를 뽑는다.
   - SIFT, SuperPoint/SuperGlue, ALIKED/LightGlue, VGGSfM tracker 등으로 feature matching/tracking을 수행한다.
   - VGGT initialization, COLMAP, geometric post-filtering, ensemble classifier로 camera/depth pseudo-label 품질을 보수적으로 검증한다.

6. Self-supervised learning
   - Supervised VGGT-$\Omega$ checkpoint에서 teacher/student를 초기화한다.
   - 같은 frame set에 서로 다른 augmentation, frame permutation, masking을 적용한다.
   - Student는 teacher의 feature distribution과 camera/depth prediction을 맞춘다.
   - Teacher는 EMA로만 업데이트한다.
   - Collapse 방지를 위해 self-supervised stage에서는 camera/depth head를 freeze한다.

### 7. Mathematical background

기본 prediction 함수는 다음과 같다.

$$
((g_1,D_1), \ldots, (g_N,D_N)) = f(I_1,\ldots,I_N)
$$

Camera parameter는 다음처럼 표현한다.

$$
g_i = (q_i,t_i,f_i), \quad q_i \in \mathbb{R}^4,\ t_i \in \mathbb{R}^3,\ f_i \in \mathbb{R}^2
$$

Training objective는 multi-task loss다.

$$
\mathcal{L}
= \lambda_{\mathrm{cam}}\mathcal{L}_{\mathrm{cam}}
+ \lambda_{\mathrm{depth}}\mathcal{L}_{\mathrm{depth}}
+ \lambda_{\mathrm{point}}\mathcal{L}_{\mathrm{point}}
+ \lambda_{\mathrm{match}}\mathcal{L}_{\mathrm{match}}
$$

Supplement 기준 loss weight는 다음과 같다.

$$
\lambda_{\mathrm{cam}}=5.0,\quad
\lambda_{\mathrm{depth}}=1.0,\quad
\lambda_{\mathrm{point}}=0.5,\quad
\lambda_{\mathrm{match}}=0.1
$$

Camera loss는 VGGT의 Huber loss 대신 $\ell_1$ objective를 사용한다. 논문은 이것이 더 stable하다고 보고한다.

Depth loss는 aleatoric uncertainty와 gradient consistency를 포함한다. Point loss는 point map을 직접 예측하지 않고, depth와 camera의 unprojection으로 만든 point residual에 depth loss와 유사한 형태의 loss를 적용한다.

$$
e_i = \pi^{-1}(\hat{D}_i,\hat{g}_i) - P_i
$$

여기서 $\pi^{-1}$는 unprojection, $P_i$는 ground-truth point map이다. Matching loss는 3D location이 같은 positive token pair의 cosine similarity를 높이고, geometric/appearance constraint로 고른 negative pair의 similarity를 낮추는 weighted binary cross-entropy다.

Scaling evaluation에서는 predicted depth를 camera로 unproject해 3D point를 만들고, ground truth point와의 $\ell_2$ distance를 point error로 사용한다. Chamfer distance 대신 point error를 택한 이유는 unordered point set nearest-neighbor matching이 wall/floor 같은 큰 surface region에 지배될 수 있기 때문이다.

### 8. Experiments

Implementation detail은 매우 크다. Model variant는 200M, 500M, 1B, 10B parameter이고, alternating-attention block 수와 hidden size는 각각 $12/12/24/16$, $384/768/1024/4096$이다. ViT는 DINOv3로 초기화하며 freeze하지 않는다. Training은 AdamW, 240K iteration으로 구성되고, 160K supervised, 50K self-supervised, 마지막 30K supervised stage를 사용한다. Batch마다 frame 수는 $[1,24]$에서 sample하고, image area는 대략 $512 \times 512$로 맞춘다. Training에는 128개 96GB H100 GPU, bfloat16, gradient checkpointing, FSDP를 사용한다.

Benchmark는 static dataset 7 Scenes, NRGBD, ETH3D와 dynamic dataset DyCheck, Sintel, TUM-Dynamic을 사용한다. 각 scene/sequence에서 10 frame을 random sample한다. Camera pose는 relative rotation/translation error threshold curve 아래 면적인 AUC@3/AUC@30으로 측정한다. Depth는 $\delta_{1.25}$와 AbsRel을 사용한다.

주요 결과는 다음과 같다.

| 평가 | 대표 수치 | 해석 |
|---|---:|---|
| Sintel camera pose | Ours-10B AUC@3 $40.0$ vs MegaSaM $22.5$ | 기존 최고 대비 77% relative improvement |
| Sintel camera pose | Ours-10B AUC@30 $79.1$ vs MegaSaM $58.3$ | relaxed threshold에서도 큰 격차 |
| Sintel depth | Ours-10B $\delta_{1.25}=93.5$, AbsRel $0.081$ | DA3 $86.1/0.118$ 대비 개선 |
| ETH3D camera pose | Ours-10B AUC@3/AUC@30 $56.3/90.4$ | wide-baseline static scene에서도 강함 |
| NRGBD depth | Ours-10B $\delta_{1.25}=99.7$, AbsRel $0.007$ | near-saturated benchmark에서도 개선 |
| TUM-Dynamic depth | Ours-10B $\delta_{1.25}=98.3$, AbsRel $0.035$ | dynamic RGB-D setting에서도 강함 |

Ablation은 논문 메시지를 잘 뒷받침한다.

| Ablation | 결과 | 의미 |
|---|---:|---|
| Model scaling | 0.2B to 10B에서 point error $0.107 \rightarrow 0.046$ | Parameter scaling이 reconstruction에도 작동 |
| Data scaling | 2K to 2M sequence에서 point error $0.275 \rightarrow 0.073$ | Data scaling이 단조 개선 |
| Register attention 25% | point error $0.073$ vs global-only $0.071$ | 성능 거의 유지하며 효율 개선 |
| Point/matching loss 제거 | point error $0.078$ | Training-only multi-task supervision은 필요 |
| Self-supervised step 10% | point error $0.073 \rightarrow 0.070$ | unlabeled video는 OOD generalization에 도움 |
| Original VGGT multi-head setup | point error $0.070$ | 약간 좋지만 dense head가 많아 scaling에는 불리 |

Annotation pipeline quality도 중요한 실험이다. Sintel에서 filtering 기준을 만족하는 sequence/pixel만 비교했을 때, VGGT-$\Omega$ annotation pipeline은 camera pose AUC@30 $96.4\%$, depth $\delta_{1.25}=99.3\%$를 얻고, MegaSaM은 각각 $62.1\%$, $77.2\%$다. 논문은 yield를 늘리는 것보다 확실히 맞는 pseudo-label만 남기는 보수적 filtering이 더 유리하다고 해석한다.

Register application에서는 OpenVLA-OFT baseline success rate가 Spatial/Object/Goal/Long/Average $97.6/98.4/97.9/94.5/97.1$인데, frozen VGGT-$\Omega$ scene token을 추가하면 $99.3/99.2/99.0/96.7/98.5$가 된다. 절대 개선 폭은 크지 않지만, 이미 강한 VLA baseline에서 frozen geometry register만 추가해 일관된 개선을 얻었다는 점이 중요하다.

### 9. Limitations and future work

논문이 명시한 failure case는 다음과 같다.

1. Strong motion blur에서 성능이 크게 떨어진다.
2. Field of view가 급격히 변하는 경우, 예를 들어 몇 초 사이 $10^\circ$에서 $160^\circ$로 바뀌는 경우 reconstruction quality가 저하된다.
3. Highly distorted camera에서 품질이 떨어진다.
4. Early training stage의 noisy data 영향으로, monitor가 많은 office scene 같은 경우 prediction이 불안정할 수 있다.
5. Privacy/licensing 때문에 face/trademark가 masked or blurred된 training data가 있고, 이 영역에서 depth artifact나 unstable prediction이 드물게 생길 수 있다.

Supplement의 data issue 논의도 deployment 관점에서 중요하다.

- Sensor dataset에서는 foreground-background depth leakage가 생길 수 있다.
- Thin structure는 synthetic data에서도 depth label이 wall/floor/background로 잘못 붙을 수 있다.
- HDRI dome/fake background depth가 실제 scene geometry처럼 학습될 위험이 있다.
- COLMAP/MegaSaM/ViPE로 만든 pseudo ground truth에는 doming effect가 생길 수 있다.
- Near-static street-view video에서 움직이는 사람이 wall/building에 흡수되는 "humans in walls" failure가 나타난다.
- Window 밖 geometry처럼 dataset별 depth semantics가 불일치하는 경우 model behavior가 혼란스러워질 수 있다.

Robotics 관점의 추가 한계는 다음과 같다.

- Metric scale은 여전히 외부 calibration 또는 known scale과 결합해야 한다.
- Robot wrist camera의 motion blur, rolling shutter, specular/transparent object, low-texture industrial scene은 논문 benchmark와 다를 수 있다.
- VLA 개선은 LIBERO offline benchmark에서 frozen token을 추가한 결과이며, 실제 closed-loop robot deployment robustness는 별도 검증이 필요하다.
- 10B model은 연구적으로 강하지만 onboard deployment에는 memory/latency budget이 부담될 수 있다.
- Register attention only variant는 on-device 가능성을 보이지만 accuracy trade-off가 크다.

Future work로는 wide-FOV/fisheye calibration-aware finetuning, robot proprioception/IMU/depth/LiDAR auxiliary input을 finetuning stage에서 조건부로 넣는 방법, long-horizon online memory, uncertainty-aware SLAM coupling, dynamic object decomposition, self-supervised reconstruction from scratch가 자연스럽다.

### 10. 결론

VGGT-$\Omega$는 feed-forward 3D reconstruction을 foundation-model scaling 관점에서 다룬 논문이다. Architecture는 register attention과 single dense head로 단순화하고, data는 static/dynamic 4M supervised sequence와 18M unlabeled video로 확장하며, 결과적으로 static/dynamic camera pose와 depth benchmark에서 큰 폭의 개선을 보인다.

가장 중요한 메시지는 두 가지다. 첫째, reconstruction accuracy가 model/data scale에 따라 예측 가능하게 개선되므로, 3D geometry model에도 scaling law적 관점이 유효할 가능성이 있다. 둘째, reconstruction-trained register는 VLA와 language alignment에도 유용해, 3D/4D reconstruction이 embodied spatial understanding을 위한 proxy task가 될 수 있다.

Robotics 연구자에게는 VGGT-$\Omega$를 "완성된 SLAM replacement"보다는 "강한 feed-forward geometry initializer이자 spatial representation backbone"으로 읽는 것이 적절하다. 실제 robot system에서는 BA/SLAM, calibration, metric scale, temporal consistency, sensor fusion과 결합할 때 가치가 가장 클 가능성이 높다.

## 추가 질문과 답변
