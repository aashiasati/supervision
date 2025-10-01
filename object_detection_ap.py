# 📦 Object Detection – Precision & Average Precision (AP) Calculator
# Author: Aashi Asati
# Hacktoberfest 2025
# Description: Calculate Precision, Recall, and AP for object detection predictions

def compute_iou(box1, box2):
    """
    Compute Intersection over Union (IoU) between two bounding boxes
    Each box: [x1, y1, x2, y2]
    """
    x_left = max(box1[0], box2[0])
    y_top = max(box1[1], box2[1])
    x_right = min(box1[2], box2[2])
    y_bottom = min(box1[3], box2[3])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])

    iou = intersection_area / float(box1_area + box2_area - intersection_area)
    return iou

def precision_recall_ap(pred_boxes, gt_boxes, iou_threshold=0.5):
    """
    Compute precision, recall, and approximate average precision (AP)
    pred_boxes: list of predicted boxes
    gt_boxes: list of ground truth boxes
    """
    tp = 0  # true positives
    fp = 0  # false positives
    matched_gt = set()

    for pred in pred_boxes:
        matched = False
        for i, gt in enumerate(gt_boxes):
            if i in matched_gt:
                continue
            iou = compute_iou(pred, gt)
            if iou >= iou_threshold:
                tp += 1
                matched_gt.add(i)
                matched = True
                break
        if not matched:
            fp += 1

    fn = len(gt_boxes) - tp  # false negatives

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    ap = precision * recall  # simplified approximation

    return precision, recall, ap

def main():
    # Example ground truth and predicted boxes
    gt_boxes = [[50, 50, 150, 150], [30, 30, 70, 70]]
    pred_boxes = [[48, 48, 152, 152], [25, 25, 70, 70], [200, 200, 250, 250]]

    precision, recall, ap = precision_recall_ap(pred_boxes, gt_boxes)

    print(f"✅ Precision: {precision:.2f}")
    print(f"✅ Recall: {recall:.2f}")
    print(f"✅ Approximate AP: {ap:.2f}")

if _name_ == "_main_":
    main()
